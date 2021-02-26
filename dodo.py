"""https://github.com/jupyterlab/jupyterlab@master
https://github.com/jupyterlab/lumino@master
"""
repos = list(filter(bool, __doc__.splitlines()))
# add targets to the docstring to include in the dev build.
def task_clone():
    return dict(
        tasks=list(map("git clone {}".format, repos)),
        targets=[x.rpartition("@")[0].rpartition("/")[0] for x in repos]
    )

def task_link():
    """jupter labextension link changes across the repos"""
    # find the changes in the repos relative to master.
    # go to the direction and links the packages.
    return dict(task_deps=["clone"], tasks=[])

def task_config():
    """merge config"""
    # hoist the configurations from the existing repos like jupyterlab.
    # we'll use their start to begin with.
    return dict(tasks=[
        """cp jupyterlab/jupyterlab/binder/start .
        cp jupyterlab/jupyterlab/binder/jupyter_notebook_config.py .""".splitlines()
        # can i just run their postBuild too?
    ])