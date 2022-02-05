import nox
import time

@nox.session(
    venv_backend="mamba",
    reuse_venv=True)
def test(session):
    # session.conda_install('nodejs=16', channel="conda-forge")
    session.conda_install('yarn', channel="conda-forge")
    session.install("-r", "requirements.txt")
    session.run('yarn', 'install')
    session.run('yarn', 'playwright', 'install', 'chromium')
    session.run('yarn', 'run', 'test')
