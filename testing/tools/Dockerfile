#
# Dockerfile for jupyter/accessibility development
#
# Usage:
# -------
#
# From the root of the project:
# docker build --rm -f "./testing/tools/gitpod/Dockerfile" -t <build-tag> "."
#
# To run the image:
# docker run --rm -it <build-tag>
# This image is based on: Ubuntu 20.04 (focal)
# https://hub.docker.com/_/ubuntu/?tab=tags&name=focal
# OS/ARCH: linux/amd64

FROM gitpod/workspace-base:latest

ARG MAMBAFORGE_VERSION="4.10.0-0"
ARG CONDA_ENV=a11y-tests
ARG DEBIAN_FRONTEND=noninteractive
# making this an argument for flexibility
ARG JUPYTER_APP=jupyterlab

# ---- Configure environment ----
# base HOME for all things in gitpod
ENV GITPOD_HOME=/home/gitpod \
    WORKSPACE=/workspace/a11y

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
    # software-properties-common \
    # locales \
    # wget \
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
# ---- Installing mamba  ----
RUN wget -q -O mambaforge3.sh \
    "https://github.com/conda-forge/miniforge/releases/download/$MAMBAFORGE_VERSION/Mambaforge-$MAMBAFORGE_VERSION-Linux-x86_64.sh" && \
    bash mambaforge3.sh -p ${CONDA_DIR} -b && \
    rm mambaforge3.sh && \
    fix-permissions "${CONDA_DIR}"

# -----------------------------------------------------------------------------
# ---- Copy conda and config files ----
# Copy conda environment file into the container - this needs to exists inside
# the container to create a conda environment from it
# basic workspace configurations
COPY ./testing/tools/workspace_config /usr/local/bin/workspace_config
COPY ./testing/tools/fix_permissions /usr/local/bin/fix_permissions
COPY "${JUPYTER_APP_DIR}/environment.yml" /tmp/environment.yml

RUN chmod a+rx /usr/local/bin/workspace_config && \
    chmod a+rx /usr/local/bin/fix_permissions && \
    workspace_config

# -----------------------------------------------------------------------------
# ---- Create conda environment with base dependencies ----
# Install dependencies

RUN mamba env create -f /tmp/environment.yml \
    --root-prefix="${CONDA_DIR}" \
    --prefix="${CONDA_DIR}" && \
    conda activate ${CONDA_ENV}  && \
    conda clean --all -f -y && \
    sudo rm -rf /tmp/* && \
    echo node --version ">" `node --version` && \
    fix-permissions "${CONDA_DIR}"

RUN conda activate ${CONDA_ENV} && \
    npx playwright install-deps && \
    npm cache clean --force

# -----------------------------------------------------------------------------
# Always make sure we are not root
USER gitpod
