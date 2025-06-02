# hash:sha256:5eba498a097fcd97d38d03874c2dcfa11418b2bdc03cc495fb147afc51ed45ef
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/ubuntu-desktop-igv-fiji-mambaforge:23.1.0-4-python3.10.12-fiji20231107-1617-firefox120.0-igv2.16.1-guacamole1.5.2-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN mamba install -y \
        cython==3.1.1 \
        dask==2025.5.1 \
        h5py==3.13.0 \
        joblib==1.4.2 \
        matplotlib==3.10.3 \
        numpy==2.2.6 \
        pillow==11.2.1 \
        pip==25.1.1 \
        pyopengl==3.1.9 \
        pyqt==5.15.11 \
        pyqtwebengine==5.15.11 \
        pytest==8.3.5 \
        python==3.11.0 \
        qtconsole==5.6.1 \
        requests==2.31.0 \
        responses==0.25.7 \
        scikit-learn==1.6.1 \
        scipy==1.15.2 \
        traitlets==5.13.0 \
    && mamba clean -ya

RUN pip install -U --no-cache-dir \
    -e git+https://github.com/cortex-lab/phy.git@7a2494be37a47f26f1f87e1ad3e022823f0f3dd1#egg=phy
