from pydantic import BaseModel, Field
from pathlib import Path
from shutil import copytree

A11Y = Path().parent
DOIT_CONFIG = dict(verbosity=2, list=dict(status=True, subtasks=True))
ENV = dict(
    NODE_OPTS="--max-old-space-size=4096",
    PIP_DISABLE_PIP_VERSION_CHECK="1",
    # PIP_IGNORE_INSTALLED="1",
    PIP_NO_BUILD_ISOLATION="1",
    PIP_NO_DEPENDENCIES="1",
    PYTHONIOENCODING="utf-8",
    PYTHONUNBUFFERED="1",
)


def do(*args, cwd=A11Y, **kwargs):
    """wrap a Action for consistency"""
    from os import environ
    from shlex import split
    from doit.tools import CmdAction

    if len(args) == 1:
        args = split(args[0])
    kwargs.setdefault("env", {})
    kwargs["env"] = dict(environ)
    # kwargs["env"].update(ENV)
    return CmdAction(list(map(str, args)), shell=False, cwd=str(Path(cwd).resolve()), **kwargs)


def rmdir(*dir):
    """remove a directory during the clean stage"""
    from shutil import rmtree

    for dir in dir:
        rmtree(dir, True)
        print(f"removed directory: {dir}")


def mv(src, target):
    copytree(src, target, dirs_exist_ok=True)


class Base(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        getattr(self, "__post_init__", lambda: None)()


class Main(Base):
    ids: list[str]
    dir: Path = Path("jupyter-a11y-build")
    project: type = None
    app: object = None

    def __post_init__(self):
        self.setup_project()

    @classmethod
    def get_parser(cls):
        from argparse import ArgumentParser

        parser = ArgumentParser("builder")
        parser.add_argument("-i", "--ids", help="repository ids", nargs="*")
        parser.add_argument("-d", "--dir", help="the build directory", nargs="*")
        return parser

    @classmethod
    def parse_args(cls, args=None):
        parser = cls.get_parser()
        return parser.parse_known_args(args=prep_args(args))

    def setup_project(self):
        from .project import Project

        self.project = Project(**self.dict(exclude={"project", "app"}))

    def main(self, args=None, standalone=False):
        self.setup_project()
        try:
            self.project.doit().run(prep_args(args))
        except standalone and SystemExit or () as e:
            if e.args[0] != 0:
                raise e

    @classmethod
    def run(cls, args=None, standalone=False):
        ns, args = cls.parse_args(args)
        main = cls(**ns.__dict__)
        main.main(args, standalone=standalone)

    def activate_extension(self):
        from IPython import get_ipython
        from doit import load_ipython_extension

        shell = get_ipython()
        ns = shell.user_ns
        load_ipython_extension(shell)
        ns.update((k, getattr(self, k)) for k in dir(self) if k.startswith("task_"))
        ns.update(DOIT_CONFIG=DOIT_CONFIG)


def prep_args(x):
    if x is None:
        return x
    if isinstance(x, str):
        from shlex import split

        return split(x)
    return x
