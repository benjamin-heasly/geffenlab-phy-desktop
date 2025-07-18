# This runs in an Ubuntu environment.
FROM ubuntu:22.04

# Install wget and https certificate info, which we'll use to install things, below.
# Install git for obtaining phy itself.
# Install mesa-utils-extra libegl1-mesa for OpenGL support that Phy needs.
# Clean up cache and temp files along the way.
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt update \
    && apt install --no-install-recommends --yes wget ca-certificates git mesa-utils-extra libegl1-mesa \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Install conda.
RUN mkdir -p /opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py311_24.5.0-0-Linux-x86_64.sh -O /opt/conda/miniconda.sh \
    && bash /opt/conda/miniconda.sh -b -p /opt/miniconda

# Create our conda environment from environment.yml.
COPY environment/environment.yml /opt/environment/environment.yml
RUN /opt/miniconda/bin/conda env create -f /opt/environment/environment.yml

# Include all of our code/* in /opt/code
COPY code /opt/code
COPY code/conda_run /usr/local/bin/conda_run

# Phy will try to write to these dirs when root, or no user home is configured.
RUN mkdir /.phy && chmod a+w /.phy
RUN mkdir /.config && chmod a+w /.config
RUN mkdir /.local && chmod a+w /.local

# Give Fontconfig a writable, user-independent cache directory.
# https://specifications.freedesktop.org/basedir-spec/latest/index.html
ENV XDG_CACHE_HOME=/tmp/xdg_cache
RUN mkdir $XDG_CACHE_HOME && chmod a+w $XDG_CACHE_HOME
