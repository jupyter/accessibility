#!/usr/bin/env doit -f
"""https://github.com/jupyterlab/jupyterlab@master
https://github.com/jupyterlab/lumino@master
"""
import pathlib
import doit
repos = list(filter(bool, __doc__.splitlines()))

def repo_to_path(x):
    """extract the local checkout name"""
    return pathlib.Path(x.rpartition("@")[0].rpartition("/")[2])

# add targets to the docstring to include in the dev build.
def task_clone():
    """clone all the repos defined in the doc string"""
    for repo in repos:
        yield dict(
            name=f"clone_{repo}",
            actions=[f"git clone {repo}"],
            targets=[repo_to_path(repo) / "package.json"]
        )

def task_build():
    """ensure a working build of live development builds"""
    print(repos)
    for dep in [repo_to_path(x) / "package.json" for x in repos]:
        print(dep)
        yield dict(
            name=f"install_{dep}",
            file_dep=[dep],
            actions=[
                f"""cd {dep.parent} 
                && jlpm --prefer-offline --ignore-optional"""
            ], 
            targets=[dep.parent / "node_modules/.yarn-integrity"]
        )
        yield dict(
            name=f"build_{dep}",
            file_dep=[dep.parent / "node_modules/.yarn-integrity"],
            actions=[
                f"""cd {dep.parent}
                && jlpm build"""
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
                cd lumino/packages/{pkg.parent.name}
                && jlpm link
                && touch ../build/link.lumino.{pkg.parent.name}.ok
                """.strip().splitlines(),
            targets=[f"build/link.lumino.{pkg.parent.name}.ok"]
        )
        yield dict(
            name=f"link_lab_{pkg.parent.name}",
            file_dep=[f"build/link.lumino.{pkg.parent.name}.ok"],         
            actions=f"""
                cd jupyterlab
                && jlpm link @lumino/{pkg.parent.name}
                && touch ../build/link.lab.{pkg.parent.name}.ok
                """.strip().splitlines(),
            targets=[f"build/link.lab.{pkg.parent.name}.ok"]
        )

def task_config():
    """merge config"""
    # hoist the configurations from the existing repos like jupyterlab.
    # we'll use their start to begin with.
    return dict(actions="""cp jupyterlab/jupyterlab/binder/start .
        cp jupyterlab/jupyterlab/binder/jupyter_notebook_config.py .""".splitlines())

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