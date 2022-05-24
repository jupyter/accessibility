"""tasks for building jupyterlab applications

it currently builds lumino and jupyterlab.

it should load extensions and retrolab.
it should export a lite build.
"""

from inspect import getmro
from json import loads
from os import environ
from pathlib import Path
from typing import List, Union

from .dodo import Base, Field, Tasks, do, mv, rmdir

CI = environ.get("CI")
GITPOD = "GITPOD_WORKSPACE_ID" in environ

if (CI is True) or (CI == "true"):
    CI = True

CI = bool(CI)

HERE = Path()
THIS = Path(__file__).parent

AXE_TEMPLATE = THIS / "jupyter-axe"
from doit.tools import create_folder


def invoke_protocol(self, protocol):
    t = type(self)

    for cls in reversed(getmro(t)):
        ns = vars(cls)
        method = ns.get(protocol)
        if method is not None:
            yield from method(self)


class Project(Tasks, Base):
    """a project is specific directory that holds source code, environments,
    built artifacts and diagnostics.

    it manages python and node environments including symbollic links to development code."""

    ids: List[str] = Field(description="shorthand for built and development resources")
    repos: dict = Field(
        default_factory=dict, description="a mapping of a product name to a Repo or Package"
    )
    dir: Path = Field(
        Path("jupyter-a11y-build"), description="the folder we want to build our application in"
    )
    env: Path = Field(
        Path(".env"), description="the folder in the dir where our conda environment will live"
    )
    links: Path = Field(
        Path("yarn-links"),
        description="the folder we use to hold our yarn symlinks for development assets",
    )
    prefix: Path = Field(None, description="a computed location for our conda environment")
    # this is why we don't need to nox, this exposes more knobs for special cases.
    conda: Union[bool, str] = Field(
        None, description="the conda run prefix used to execute isolated system commands"
    )
    # with this we can turn conda, node, and pip in offline mode
    offline: bool = Field(False, description="build in offline mode using your caches")
    yarn_links: Path = Field(None, description="the computed location of our yarn symbollic links")
    test_results: Path = Field(
        None, description="the computed location of our playwright test results"
    )

    def __post_init__(self):
        # compute the prefix and carry the absolute position forward
        self.prefix = (self.dir / self.env).resolve()

        # compute our conda run statement that prepends all the calls we make
        if self.conda is None:
            self.conda = f"conda run --no-capture-output --prefix {self.prefix}"
            if self.offline:
                self.conda += " --offline"
        elif not self.conda:
            # the empty string case is the escape hatch from using conda.
            # under these conditions you are using the environment you are in
            self.conda = ""
        # compute the location of the yarn links we manage
        self.yarn_links = (self.dir / self.links).resolve()

        # the output location of the test results for easy access
        self.test_results = self.dir / AXE_TEMPLATE.name / "test-results"

        # initialize each of the Package/Repo objects that contain
        # instructions for executing things
        for id in self.ids:
            kwargs = {}
            if "://" in id:
                # currently, everything at a url is assumed to be a repo
                # there are certainly causes where we are wrong. we might
                # likely need adapters for different network locations.

                if "@" in id:
                    id, _, branch = id.rpartition("@")
                    kwargs.setdefault("branch", branch)
                repo = Repo(url=id, parent=self, **kwargs)
            else:
                # otherwise we assume a built package.
                repo = Package(name=id, parent=self)

            self.repos[repo.name] = repo

    # this is a setup task and the description could be improved
    def task_env(self):
        """create a conda environment for development work"""
        yield self.conda and dict(
            name="conda",
            actions=[
                do(
                    f'conda create -yc conda-forge --prefix {self.prefix} python=3.9 "nodejs>=14,<15" yarn git'
                ),
                do(f"{self.conda} python -m pip install pip --upgrade"),
            ],
            uptodate=[self.prefix.exists()],
            clean=[(rmdir, [self.prefix])],
        ) or dict(name="conda", actions=None)

    def task_meta(self):
        # the meta task compiles individual tasks defined per repo/package
        # all the tasks have basename/name pairs so meta doesn't appear in the task list
        for x in self.repos.values():
            yield from invoke_protocol(x, "tasks")

    def axe_results(self):
        """load axe results from the tests and show them as a data frame"""
        import pandas

        files = list(self.test_results.rglob("axe-results.json"))
        return pandas.concat(dict(zip(files, map(pandas.read_json, files))))


class Common(Base):
    """common fields in Repo/Package classes"""

    name: str = Field(None, description="the canonical package name (eg jupyterlab, retrolab)")
    parent: Project = Field(description="the parent project orchestrating things")
    conda: str = Field(None, description="the parent's conda prefix used to execute our tasks")
    dir: Path = Field(None, description="the parent's directory we are working in ")

    def tests(self):
        yield from ()

    def tasks(self):
        yield from invoke_protocol(self, "tests")

    _EXTENSIONS = None  # extension base classes define there own mapping ot manage

    def __init_subclass__(cls, id=None):
        if id:
            # register a baseclass for a jupyter product
            cls._EXTENSIONS[id] = cls

    def __new__(cls, *args, **kwargs):
        """the new method discovers the proper baseclass for the EXTENSION"""
        repo = super(type, cls).__new__(cls)
        repo.__init__(*args, **kwargs)
        if cls in {Repo, Package} and repo.name in cls._EXTENSIONS:
            # choose to make a poackage or repo
            return super().__new__(cls._EXTENSIONS[repo.name])
        return repo


class Package(Common):
    """the base class of all packages

    packages are built and available on package managers. the id `jupyterlab` is the `jupyterlab` package in `pip`"""

    _EXTENSIONS = {}  # extension base classes define there own mapping ot manage

    def tasks(self):
        yield dict(
            basename="setup",
            name=f"pip:{self.name}",
            actions=[do(f"{self.conda} python -m pip install {self.name}")],
            clean=[do(f"{self.conda} python -m pip uninstall -y {self.name}")],
        )

    def __post_init__(self):
        # propogate parent content to package
        self.dir = self.parent.dir
        self.conda = self.parent.conda


PIP_BUILD_ENV = dict(
    NODE_OPTS="--max-old-space-size=4096",
    PIP_DISABLE_PIP_VERSION_CHECK="1",
    # PIP_IGNORE_INSTALLED="1",
    PIP_NO_BUILD_ISOLATION="1",
    # PIP_NO_DEPENDENCIES="1",
    PYTHONIOENCODING="utf-8",
    PYTHONUNBUFFERED="1",
)


class Repo(Common):
    """the base class for all repos

    repos need instructions to build jupyter products, they are defined as doit tasks in each class.
    these repos needed to be cloned, dev dependencies built.
    """

    _EXTENSIONS = {}
    url: str = Field(description="the url for the project pointing to a git repo")
    branch: str = Field("main", description="the branch, ref, or hash to build")
    path: Path = Field(None, description="path the repository with a git repo")
    head: Path = Field(None, description="the HEAD of the git repo")
    package: Path = Field(None, description="the package.json")
    links: Path = Field(None, description="the yarn links location")
    pip: str = Field(None, description="the pip command prefix including conda")
    yarn: Path = Field(None, description="yarn prefix including conda")
    yarn_integrity: Path = Field(None, description="the location of the yarn integrity file")
    # useful for hashing
    setup: Path = Field(None, description="the setup.py target")  # assuming one is being used

    def __post_init__(self):
        self.name = get_name(self.url)
        self.dir = self.parent.dir
        self.path = self.dir / self.name
        self.head = self.path / ".git" / "HEAD"
        self.package = self.path / "package.json"
        self.links = self.path / "yarn-links"
        self.conda = self.parent.conda
        self.yarn = f"{self.conda} yarn --link-folder {self.links.resolve()}"
        self.pip = f"{self.conda} python -m pip"
        self.yarn_integrity = self.path / "node_modules" / ".yarn-integrity"
        self.setup = self.path / "setup.py"

    def get_packages(self, where="packages"):
        """yield package.json from all folders one level down"""
        # this requires the repos are setup/cloned
        yield from (self.path / where).rglob("*/package.json")

    # cloning requires the env
    # everything else requires cloning
    def clone(self, depth=1):
        """create a task to clone a repo
        the previous version did some more complicated things we might want to revive."""
        # it would be a better development experience to construct the git repository
        # explicitly relative to a commit.

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

    # this task needs to be generated after cloing
    def yarn_install(self, link=True):
        """install the yarn package"""
        # link_to are urls to repos, they are managed by the parent class
        yield dict(
            basename="install",
            name=f"yarn:{self.name}",
            file_dep=[self.package, self.head],
            actions=[(create_folder, [self.links]), do(self.yarn, cwd=self.path)],
            targets=[self.yarn_integrity],
        )

        if link:
            yield from self.new_symlinks()

    # yarn links are symbollic links to development packages like python edittable methods.
    def new_symlinks(self, *deps):
        """created symbollic links to development packages"""
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
        """created symbollic links to local development dependencies created by new_symlinks"""

        visited = set()
        for package in self.get_packages():
            data = loads(package.read_text(encoding="utf-8"))
            name = data["name"]
            if name not in visited:
                visited.add(name)
                # should use basename
                yield dict(
                    basename="install",
                    name=f"yarn:link:close:{name}",
                    file_dep=[package],
                    actions=[do(f"yarn link --link-folder {self.links} {name}", cwd=target.path)],
                    targets=[target.links / name / "package.json"],
                )

    def pip_install(self):
        """pip install the python package"""
        yield dict(
            basename="install",
            name=f"pip:{self.name}",
            actions=[
                do(f"{self.conda} python -m pip install jupyter_packaging"),
                do(
                    f"{self.conda} python -m pip install -e.",  # many settings are held in the env
                    cwd=self.path,
                    env=PIP_BUILD_ENV,
                ),
            ],
        )

    def tasks(self):
        yield self.clone()
        # we need to clone before we can do anything
        # these have to happen afterwards. the order in the method has no bearing on the execution order
        yield self.yarn_install()

    def get_repo(self, id):
        if isinstance(id, type):
            id = id.id

        return self.parent.repos[id]


# documentation tests and unit tests would have different task specifications
class PlayWrightTests:
    """a mixin with playwright tests"""

    def tests(self):
        target = self.dir / AXE_TEMPLATE.name
        yield dict(
            basename="test_setup",
            name="copy-templates",
            actions=[(mv, [AXE_TEMPLATE, target])],
            clean=[(rmdir, [target])],
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
        if CI or GITPOD:
            # i dont know how to measure the state of playwright browsers. this measure should go in the
            # uptodate attribute of the task. currently, we're just using whatever logic. in theory, we could
            # just run this and rely on whatever caching playwright does.
            # why are there so many browsers?
            yield dict(
                basename="test_setup",
                name="playwright",
                actions=[
                    do(f"{self.conda} npx playwright install --with-deps chromium", cwd=target)
                ],
            )
        yield dict(
            basename="test",
            name="playwright",
            actions=[
                do(f"echo 'the target is {target.absolute()}'"),
                do(f"{self.conda} npx playwright test", cwd=target),
            ],
        )


class JupyterApplication(Common, PlayWrightTests):
    pass


class JupyterLabPackage(Package, JupyterApplication, id="jupyterlab"):
    pass


class RetroLabPackage(Package, JupyterApplication, id="retrolab"):
    """a class for the retrolab package from pypi"""


class JupyterLabRepo(Repo, JupyterApplication, id="jupyterlab"):
    """a class for the jupyterlab package from pypi"""

    branch: str = "master"

    def tasks(self):
        if "lumino" in self.parent.repos:
            yield from self.parent.repos["lumino"].close_yarn_symlinks(self)

        yield self.pip_install()


class RetroLabRepo(Repo, JupyterApplication, id="retrolab"):
    """a class for the jupyterlab package from pypi"""

    def tasks(self):
        if "lumino" in self.parent.repos:
            pass
        if "jupyterlab" in self.parent.repos:
            pass
        yield from ()


def get_name(id):
    """get the name of a thing from a the last bit of the url"""
    return id.rpartition("/")[2]


class JupyterExtension:
    """a placeholder class for jupyter extensions when we need to test them too."""
