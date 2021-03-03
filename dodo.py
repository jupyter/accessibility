#!/usr/bin/env doit -f
"""https://github.com/jupyterlab/jupyterlab@408f30f
https://github.com/jupyterlab/lumino@09aec10
"""
# change the urls above to link different jupyter references.


import pathlib
import doit

DOIT_CONFIG = {
    "backend": "sqlite3",
    "verbosity": 2,
    "par_type": "thread",
}

HERE = pathlib.Path(__file__).parent

repos = list(filter(bool, __doc__.splitlines()))


def task_lint():
    all_py = HERE.glob("*.py")
    yield dict(
        name="py",
        file_dep=[*all_py],
        actions=[["black", "--quiet", *all_py]]
    )


# add targets to the docstring to include in the dev build.
def task_clone():
    """clone all the repos defined in the doc string"""
    for repo in repos:
        repo, _, branch = repo.rpartition("@")
        path = pathlib.Path(repo.rpartition("/")[2])
        yield dict(
            name=f"clone_{repo}",
            actions=[] if path.exists() else [f"git clone --depth 1 {repo}"],
            targets=[path / "package.json"]
        )

def task_build():
    """ensure a working build of live development builds"""
    for dep in [repo_to_path(x) / "package.json" for x in repos]:
        yield dict(
            name=f"install_{dep}",
            file_dep=[dep],
            actions=[
                f"""cd {dep.parent} && jlpm --prefer-offline --ignore-optional"""
            ],
            targets=[dep.parent / "node_modules/.yarn-integrity"]
        )
        yield dict(
            name=f"build_{dep}",
            file_dep=[dep.parent / "node_modules/.yarn-integrity"],
            actions=[
                f"""cd {dep.parent} && jlpm build"""
            ],
            targets=list(dep.parent.rglob("packages/*/lib/*.js"))
        )

def task_link_lumino():
    """jupter labextension link changes across the repos"""
    # find the changes in the repos relative to master.
    # go to the direction and links the packages.
    for pkg in pathlib.Path("lumino/packages").glob("*/package.json"):
        yield dict(
            name=f"link_lumino_{pkg.parent.name}",
            file_dep=[
                pkg,
                pkg.parent.parent.parent / "node_modules/.yarn-integrity"
            ],
            actions=f"""
                cd lumino/packages/{pkg.parent.name} \
                && jlpm link

                """.strip().splitlines(),#&& touch ../../build/link.lumino.{pkg.parent.name}.ok
            targets=[]# [f"build/link.lumino.{pkg.parent.name}.ok"]
        )
        yield dict(
            name=f"link_lab_{pkg.parent.name}",
            file_dep=[],#[f"build/link.lumino.{pkg.parent.name}.ok"],
            actions=f"""
                cd jupyterlab \
                && jlpm link @lumino/{pkg.parent.name}

                """.strip().splitlines(), #&& touch ../build/link.lab.{pkg.parent.name}.ok
            targets=[f"build/link.lab.{pkg.parent.name}.ok"]
        )

def task_config():
    """merge config"""
    # hoist the configurations from the existing repos like jupyterlab.
    # we'll use their start to begin with.
    return dict(actions="""cp jupyterlab/binder/start .
        cp jupyterlab/binder/jupyter_notebook_config.py .""".splitlines())

# def task_postBuild():
#     """recursively invoke all postBuilds"""
#     for repo in repos:
#         for postBuild in [*repo.rglob("postBuild")]:
#             yield dict(
#                 name=repo + str(postBuild),
#                 file_dep=[postBuild],
#                 actions=[
#                     doit.CmdAction([], shell=False, cwd=postBuild.parent)
#                 ]
#             )

# utilities

def repo_to_path(x):
    """extract the local checkout name"""
    return pathlib.Path(x.rpartition("@")[0].rpartition("/")[2])
