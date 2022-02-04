import nox
import time

@nox.session(venv_backend="mamba")
def ra11y(session):
    session.conda_install('nodejs=16', channel="conda-forge")
    session.conda_install('yarn', channel="conda-forge")
    session.install("-r", "requirements.txt")
    session.run('yarn', 'install')
    session.run('yarn', 'run', 'start:detached')
    time.sleep(20)
    session.run('yarn', 'run', 'test')
