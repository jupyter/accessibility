"""tasks for building jupyterlab applications

it currently builds lumino and jupyterlab.

it should load extensions and retrolab.
it should export a lite build.
"""

from pathlib import Path
from os import rmdir
from typing import List

from jupyter_accessibility.testing import AXE_TEMPLATE, DOIT_CONFIG
from .dodo import do, rmdir, Base, Field, mv
from pathlib import Path
from json import loads


PIP = ("python", "-m", "pip")
HERE = Path()
THIS = Path(__file__).parent
REPOS = ["https://github.com/jupyterlab/lumino", "https://github.com/jupyterlab/jupyterlab"]
from doit.tools import create_folder


class Project(Base):
    """a project is specific directory that holds source code, environments,
    built artifacts and diagnostics.

    it manages python and node environments including symbollic links to development code."""

    ids: List[str]
    repos: dict = Field(default_factory=dict, metadata=dict(description=""))
    dir: Path = Path("jupyter-a11y-build")
    env: Path = Path(".env")
    links: Path = Path("yarn-links")
    prefix: Path = None
    conda: str = None
    offline: bool = False
    yarn_links: Path = None
    test_results: Path = None

    def __post_init__(self):
        self.prefix = (self.dir / self.env).resolve()
        self.conda = f"conda run --no-capture-output --prefix {self.prefix}"
        if self.offline:
            self.conda += " --offline"
        self.yarn_links = (self.dir / self.links).resolve()
        self.prefix = (self.dir / self.env).resolve()
        self.test_results = (self.dir / AXE_TEMPLATE.name / "test-results")
        
        
        # initialize each of the Package/Repo objects that contain
        # instructions for executing things
        for id in self.ids:
            kwargs = {}
            if "://" not in id:
                repo = Package(name=id, parent=self)
            else:
                if "@" in id:
                    id, _, branch = id.rpartition("@")
                    kwargs.setdefault("branch", branch)
                repo = Repo(url=id, parent=self, **kwargs)
                
            self.repos[repo.name] = repo

    def task_env(self):
        """create a conda environment for development work"""
        yield dict(
            name="conda",
            actions=[
                do(
                    f'conda create -yc conda-forge --prefix {self.prefix} python=3.9 "nodejs>=14,<15" yarn git'
                ),
                do(f"{self.conda} python -m pip install pip --upgrade"),
            ],
            uptodate=[self.prefix.exists()],
            clean=[(rmdir, [self.prefix])],
        )

    def _test_build(self):
        pass

    # def task_test(self):
    #     """run accessibility unit tests against jupyter products"""
    #     yield dict(name="playwright", actions=None)
    #     yield dict(name="docs", actions=None)
    #     yield dict(name="nbconvert", actions=None)

    def task_meta(self):
        for x in self.repos.values():
            yield from x.tasks()
        # yield dict(basename="yarn_install", name="yarn_links", actions=None, task_dep=["deplink", "symlink"])
        

    def doit(self):
        from doit.cmd_base import ModuleTaskLoader
        from doit.doit_cmd import DoitMain

        tasks = dict((x, getattr(self, x)) for x in dir(self) if x.startswith("task_"))
        tasks.update({"DOIT_CONFIG": DOIT_CONFIG})
        return DoitMain(ModuleTaskLoader(tasks))

    def commands(self):
        return self.doit().get_commands()

    def do(self, x, **kwargs):
        return do(F"{self.conda} {x}", **kwargs)

    def axe_results(self):
        import pandas

        files = list(self.test_results.rglob("axe-results.json"))
        return pandas.concat(dict(zip(files, map(pandas.read_json, files))))


# after we run some tests we should be able to use this class to consume the data


_EXTENSIONS = {}

class Ext:
    _EXTENSIONS = None

    def __init_subclass__(cls, id=None):
        if id:
            cls._EXTENSIONS[id] = cls
    def __new__(cls, *args, **kwargs):
        repo = super(type, cls).__new__(cls)
        repo.__init__(*args, **kwargs)
        if cls in {Repo, Package} and repo.name in cls._EXTENSIONS:
            return super().__new__(cls._EXTENSIONS[repo.name])
        return repo        

class Common(Base):
    name: str = None
    parent: Project
    conda: str = None
    dir: Path = None


class Package(Common, Ext):
    _EXTENSIONS = {}

    def tasks(self):
        yield dict(basename="setup", name=F"pip:{self.name}", actions=[
            do(f"{self.conda} python -m pip install {self.name}")
        ])
        yield from self.tests()

    def tests(self):
        yield from ()


    def __post_init__(self):
        self.dir = self.parent.dir
        self.conda = self.parent.conda






class Repo(Common, Ext):
    _EXTENSIONS = {}
    url: str
    prefix: Path = None
    conda: str = None
    branch: str = "main"
    env: Path = None
    path: Path = None
    head: Path = None
    package: Path = None
    links: Path = None
    pip: str = None
    yarn: Path = None
    yarn_integrity: Path = None
    setup: Path = None
    setup: Path = None

    def __post_init__(self):
        self.name = get_name(self.url)
        self.dir = self.parent.dir
        self.path = self.dir / self.name
        self.prefix = self.parent.prefix
        self.head = self.path / ".git" / "HEAD"
        self.package = self.path / "package.json"
        self.links = self.path / "yarn-links"
        self.env = (self.dir / ".env").resolve()
        self.conda = self.parent.conda
        self.yarn = f"{self.conda} yarn --link-folder {self.links.resolve()}"
        self.pip = f"{self.conda} python -m pip"
        self.yarn_integrity = self.path / "node_modules" / ".yarn-integrity"
        self.setup = self.path / "setup.py"

    def get_packages(self, where="packages"):
        """yield package.json from all folders one level down"""
        yield from (self.path / where).rglob("*/package.json")

    # cloning requires the env
    # everything else requires cloning
    def clone(self, depth=1):
        """create a task to clone a repo
        the previous version did some more complicated things we might want to revive."""
        # it would be a better development experience to construct the git repository
        # explicitly relative to a commit.

        if self.local:
            # when working on local version of the repository we clone it
            yield dict(
                basename="setup",
                name=self.name,
                actions=[
                    (create_folder, [self.path]),
                    f"""{self.conda} git clone --depth {depth} --branch {self.branch} {self.url} {self.path}""",
                ],
                targets=[self.head],
                clean=[f"rm -rf {self.path.absolute()}"],
                uptodate=[self.head.exists()],
            )

    def yarn_install(self, link=True, *link_to):
        """install the yarn package"""
        # link_to are urls to repos, they are managed by the parent class
        yield dict(
            basename="yarn_install",
            name=self.name,
            file_dep=[self.package, self.head],
            actions=[(create_folder, [self.links]), do(self.yarn, cwd=self.path)],
            targets=[self.yarn_integrity],
        )

        if link:
            yield from self.new_symlinks()

    # yarn links are symbollic links to development packages like python edittable methods.
    def new_symlinks(self, *deps):
        visited = set()

        for package in self.get_packages():
            data = loads(package.read_text(encoding="utf-8"))
            name = data["name"]
            if name not in visited:
                visited.add(name)
                yield dict(
                    basename="symlink",
                    name=name,
                    file_dep=list(deps) + [package],
                    actions=[do(f"yarn link --link-folder {self.links}", cwd=package.parent)],
                    targets=[self.links / name / "package.json"],
                )

    def close_yarn_symlinks(self, target):
        visited = set()
        for package in self.get_packages():
            data = loads(package.read_text(encoding="utf-8"))
            name = data["name"]
            if name not in visited:
                visited.add(name)
                # should use basename
                yield dict(
                    basename="deplink",
                    name=name,
                    file_dep=[package],
                    actions=[do(f"yarn link --link-folder {self.links} {name}", cwd=target.path)],
                    targets=[target.links / name / "package.json"],
                )

    def pip_install(self):
        yield dict(basename="setup", name=F"pip:{self.name}", actions=[
            do(f"{self.conda} python -m pip install packaging deprecation tomlkit jupyter_packaging"),
            do(f"{self.conda} python -m pip install --no-build-isolation -e.", cwd=self.path)
        ])

    def tasks(self):
        yield self.clone()
        # we need to clone before we can do anything
        # these have to happen afterwards
        yield self.yarn_install()

    def get_repo(self, id):
        if isinstance(id, type):
            id = id.id

        return self.parent.repos[id]

class JupyterLabPackage(Package, id="jupyterlab"):
    def tests(self):
        target = self.dir / AXE_TEMPLATE.name
        yield dict(
            basename="test_setup",
            name="copy-templates",
            actions=[(mv, [AXE_TEMPLATE, target])],
            uptodate=[target.exists()],
        )
        yield dict(
            basename="test_setup",
            name="pip",
            actions=[do(f"{self.conda} pip install -r requirements.txt", cwd=target)],
        )
        yield dict(
            basename="test_setup",
            name="yarn",
            actions=[do(f"{self.conda} yarn install", cwd=target)],
        )
        yield dict(
            basename="test_setup",
            name="browser",
            actions=[do(f"{self.conda} npx playwright install chrome", cwd=target)],
        )
        yield dict(basename="test", name="playwright", actions=[do(f"{self.conda} npx playwright test", cwd=target)])
class RetroLabPackage(JupyterLabPackage, id="retrolab"):
    pass

class JupyterLab(Repo, id="jupyterlab"):
    branch: str = "master"

    def tasks(self):
        yield from super().tasks()
        lumino = self.parent.repos["lumino"]
        yield from lumino.close_yarn_symlinks(self)
        yield self.pip_install()


def get_name(id):
    """get the name of a thing from a the last bit of the url"""
    return id.rpartition("/")[2]
