#
# Dockerfile for jupyter/accessibility development
#
# Usage:
# -------
#
# From the root of the project:
# docker build --rm -f "./tools/Dockerfile" -t <build-tag> "."
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

# ---- Configure environment ----
# base HOME for all things in gitpod
ENV GITPOD_HOME=/home/gitpod \
    WORKSPACE=/workspace/a11y

ENV CONDA_DIR="${GITPOD_HOME}/mambaforge3" \
    SHELL=/bin/bash
ENV PATH=${CONDA_DIR}/bin:$PATH

# Need to specify where we are installing the browsers
ENV PLAYWRIGHT_BROWSERS_PATH="${GITPOD_HOME}/ms-playwright" \
    NODE_DEPS_PATH="${GITPOD_HOME}/node_modules"

# -----------------------------------------------------------------------------
# ---- Creating as root - note: make sure to change to gitpod in the end ----
USER root

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
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
    rm mambaforge3.sh


# -----------------------------------------------------------------------------
# ---- Copy conda and config files ----
# Copy conda environment file into the container - this needs to exists inside
# the container to create a conda environment from it
# basic workspace configurations
COPY ./tools/gitpod/workspace_config /usr/local/bin/workspace_config
RUN chmod a+rx /usr/local/bin/workspace_config && \
    workspace_config

COPY ./tools/environment.yml /tmp/environment.yml

# -----------------------------------------------------------------------------
# ---- Create conda environment ----
# Install dependencies
RUN mamba env create -f /tmp/environment.yml && \
    conda activate ${CONDA_ENV}  && \
    conda clean --all -f -y && \
    rm -rf /tmp/* && \
    echo node --version

# -----------------------------------------------------------------------------
# ---- Copy needed files for npm dependencies ----
COPY ./tests/retrolab/package.json package.json

# Only install chromium for now - can change at build time
ARG BROWSERS="chromium"

RUN mkdir ${PLAYWRIGHT_BROWSERS_PATH}

RUN conda activate ${CONDA_ENV} && \
    rm -rf ${NODE_DEPS_PATH} && \
    npm install -g node-gyp && \
    yarn install && \
    chmod -R 777 ${PLAYWRIGHT_BROWSERS_PATH} && \
    npx playwright install-deps && \
    npx playwright install ${BROWSERS} && \
    rm package.json  && \
    rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------------------------
# Always make sure we are not root
USER gitpod
