# hash:sha256:5dcc00200f0fd8fe4d7ca41fd7a456723b6e3e312cbf88821bde00f47d45b73d
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
        'scipy traitlets' \
    && conda clean -ya
