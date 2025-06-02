# hash:sha256:3547bad8a3910fd25f904cdd99c09eedfbb625f37f08213e1e795d4567a021ac
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/ubuntu-desktop-igv-fiji-mambaforge:23.1.0-4-python3.10.12-fiji20231107-1617-firefox120.0-igv2.16.1-guacamole1.5.2-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN mamba install -y \
        cython \
        dask \
        h5py \
        joblib \
        matplotlib \
        numpy \
        pillow \
        pip==25.1.1 \
        pyopengl \
        pyqt \
        pyqtwebengine \
        pytest \
        python==3.11 \
        qtconsole \
        requests \
        responses \
        scikit-learn \
        scipy \
        traitlets \
    && mamba clean -ya

RUN pip install -U --no-cache-dir \
    -e git+https://github.com/cortex-lab/phy.git#egg=phy
