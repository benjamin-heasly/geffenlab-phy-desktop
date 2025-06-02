# hash:sha256:77c85a768aadc3c325eb8f68c52bd7a2ef64fadad468f7970d81985ec0a0fdfe
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/ubuntu-desktop-igv-fiji-mambaforge:23.1.0-4-python3.10.12-fiji20231107-1617-firefox120.0-igv2.16.1-guacamole1.5.2-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN conda install -y \
        cython \
        dask \
        h5py \
        joblib \
        matplotlib \
        numpy \
        pillow \
        pip==23.1.2 \
        pyopengl \
        pyqt \
        pyqtwebengine \
        pytest \
        python==3.10.12 \
        qtconsole \
        requests \
        responses \
        scikit-learn \
        scipy \
        traitlets \
    && conda clean -ya
