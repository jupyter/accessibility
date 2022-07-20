# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tempfile import mkdtemp

# These settings modeled after https://github.com/jupyterlab/jupyterlab/blob/%40jupyterlab/galata%404.0.2/galata/jupyter_server_test_config.py

c.ServerApp.port = 8888
c.ServerApp.port_retries = 0
c.ServerApp.open_browser = False

c.ServerApp.root_dir = mkdtemp(prefix="galata-test-")
c.ServerApp.token = ""
c.ServerApp.password = ""
c.ServerApp.disable_check_xsrf = True
c.LabApp.expose_app_in_browser = True
