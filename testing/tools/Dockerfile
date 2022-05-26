# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
#
# Dockerfile for jupyter/accessibility development
#
# Usage:
# -------
#
# From the root of the project:
# docker build --rm -f "./testing/tools/gitpod/Dockerfile" -t <build-tag> "."
#
# By default it will build for /testing/jupyterlab - to build for a different app
# docker build --build-arg JUPYTER_APP=retrolab --rm -f "./testing/tools/gitpod/Dockerfile" -t <build-tag> "."
# To run the image:
# docker run --rm -it <build-tag>
# This image is based on: Ubuntu 20.04 (focal)
# https://hub.docker.com/_/ubuntu/?tab=tags&name=focal
# OS/ARCH: linux/amd64

# pinning the version
FROM gitpod/workspace-base:2022-05-20-05-44-40

# https://github.com/conda-forge/miniforge/releases
ARG MAMBAFORGE_VERSION="4.10.0-0"
ARG CONDA_ENV=a11y-tests
# making this an argument for flexibility
ARG JUPYTER_APP=jupyterlab

# ---- Configure environment ----------
# base HOME for all things in gitpod
ENV DEBIAN_FRONTEND=noninteractive
ENV GITPOD_HOME=/home/gitpod \
    WORKSPACE=/workspace/a11y \
    USER=gitpod \
    GITPOD_GIUD=33333

ENV CONDA_DIR="${GITPOD_HOME}/mambaforge3" \
    SHELL=/bin/bash
ENV PATH=${CONDA_DIR}/bin:$PATH
ENV JUPYTER_APP_DIR="./testing/${JUPYTER_APP}"

# -----------------------------------------------------------------------------
# ---- Creating as root - note: make sure to change to gitpod in the end ----
USER root

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    software-properties-common \
    locales \
    wget \
    build-essential \
    ca-certificates \
    curl \
    dirmngr \
    make && \
    # this needs to be done after installing dirmngr
    apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0 && \
    apt-add-repository https://cli.github.com/packages && \
    apt-get install -yq --no-install-recommends \
    gh && \
    locale-gen en_US.UTF-8 && \
    # clean apt cache
    apt-get clean && \
    rm -rf /var/cache/apt/* &&\
    rm -rf /var/lib/apt/lists/* &&\
    rm -rf /tmp/*

# Allows this Dockerfile to activate conda environments
SHELL ["/bin/bash", "--login", "-o", "pipefail", "-c"]

# -----------------------------------------------------------------------------
# ---- Copy conda and config files ----
# Copy conda environment file into the container - this needs to exists inside
# the container to create a conda environment from it
COPY "${JUPYTER_APP_DIR}/environment.yml" /tmp/environment.yml
# basic workspace configurations
COPY ./testing/tools/workspace_config /usr/local/bin/workspace_config
# Copy a script that we will use to correct permissions after running certain commands
COPY ./testing/tools/fix_permissions /usr/local/bin/fix_permissions

RUN chmod a+rx /usr/local/bin/workspace_config && \
    chmod a+rx /usr/local/bin/fix_permissions && \
    workspace_config

# -----------------------------------------------------------------------------
# ---- Installing mamba  ----
RUN wget -q -O mambaforge3.sh \
    "https://github.com/conda-forge/miniforge/releases/download/$MAMBAFORGE_VERSION/Mambaforge-$MAMBAFORGE_VERSION-Linux-x86_64.sh" && \
    bash mambaforge3.sh -p ${CONDA_DIR} -b && \
    rm mambaforge3.sh && \
    fix_permissions "${CONDA_DIR}"

# -----------------------------------------------------------------------------
# ---- Create conda environment with base dependencies ----
# Install dependencies
RUN mamba env create -f /tmp/environment.yml && \
    conda clean --all -f -y && \
    rm -rf /tmp/*

RUN fix_permissions "${CONDA_DIR}" && \ 
    chown "${USER}:${GITPOD_GIUD}" "${CONDA_DIR}" 

RUN conda activate ${CONDA_ENV} && \
    # Install node dependencies
    npx playwright install-deps && \
    npm cache clean --force

# -----------------------------------------------------------------------------
# Always make sure we are not root
USER ${USER}