from pathlib import Path
from shutil import copytree

from pydantic import BaseModel

A11Y = Path().parent
DOIT_CONFIG = dict(verbosity=2, list=dict(status=True, subtasks=True), backend="json")


# a pydantic basemodel that allows for dataclass-like post init conventions.
class BaseClass(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add post init behavior because its a nice pattern and helps post initialize.
        # we were using dataclasses, but pydantic's better.
        getattr(self, "__post_init__", lambda: None)()

Base = BaseClass # remove once transition is complere

def do(*args, cwd=A11Y, **kwargs):
    """wrap a Action for consistency"""
    from os import environ
    from shlex import split

    from doit.tools import CmdAction

    if len(args) == 1:
        args = split(args[0])
    kwargs.setdefault("env", {})
    kwargs["env"] = {**environ, **kwargs["env"]}
    return CmdAction(list(map(str, args)), shell=False, cwd=str(Path(cwd).resolve()), **kwargs)


def remove_directory(*dir):
    """remove a directory during the clean stage"""
    from shutil import rmtree

    for dir in dir:
        rmtree(dir, True)
        print(f"removed directory: {dir}")


def move_directory(src, target):

    copytree(src, target, dirs_exist_ok=True)




class Main(BaseClass):
    """Main orchestrates the building and testing of jupyter products.

    It initializes the project and invokes the primary doit application."""

    ids: list[str]
    dir: Path = Path("jupyter-a11y-build")
    project: type = None
    app: object = None

    def __post_init__(self):
        self.setup_project()

    def setup_project(self):
        from .project import Project

        self.project = Project(**self.dict(exclude={"project", "app"}))

    def main(self, args=None, standalone=False):
        """invoke the doit application through an interactive api."""
        self.setup_project()
        try:
            self.project.doit().run(prep_args(args))
        except standalone and SystemExit or () as e:
            if e.args[0] != 0:
                raise e

    @classmethod
    def run(cls, args=None, standalone=False):
        """invoke the doit application as a standalone command line tool."""
        # parse the argument we know and pass the rest to the doit application.
        ns, args = cls.parse_args(args)
        main = cls(**ns.__dict__)

        main.main(args, standalone=standalone)

    @classmethod
    def get_parser(cls):
        """the argument parser for the Main cli"""
        from argparse import ArgumentParser

        parser = ArgumentParser("builder")
        parser.add_argument("-i", "--ids", default=["retrolab"], help="repository ids", nargs="*")
        parser.add_argument(
            "-d", "--dir", default=Path("jupyter-ally-build"), help="the build directory", type=Path
        )
        return parser

    @classmethod
    def parse_args(cls, args=None):
        parser = cls.get_parser()
        return parser.parse_known_args(args=prep_args(args))

    def activate_extension(self):
        from doit import load_ipython_extension
        from IPython import get_ipython

        shell = get_ipython()
        ns = shell.user_ns
        load_ipython_extension(shell)
        ns.update((k, getattr(self, k)) for k in dir(self) if k.startswith("task_"))
        ns.update(DOIT_CONFIG=DOIT_CONFIG)


class Tasks(Base):
    def doit(self):
        """build the doit application by pulling tasks from the"""
        from doit.cmd_base import ModuleTaskLoader
        from doit.doit_cmd import DoitMain

        tasks = dict((x, getattr(self, x)) for x in dir(self) if x.startswith("task_"))
        tasks.update({"DOIT_CONFIG": DOIT_CONFIG})
        return DoitMain(ModuleTaskLoader(tasks))

    def commands(self):
        """explore what doit knows"""
        return self.doit().get_commands()

    def do(self, x, **kwargs):
        """create a cmd action that can be run from the api"""
        return do(f"{self.conda} {x}", **kwargs)


def prep_args(x):
    if isinstance(x, str):
        from shlex import split

        return split(x)
    return x
