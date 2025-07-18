# geffenlab-phy-desktop

This sets up a Docker environment with [Phy](https://github.com/cortex-lab/phy) installed.

Here's how I'm building and testing this locally.  It's a bit rought at the moment, but it works and that is a good start.

```
cd geffenlab-phy-desktop

wget https://codeload.github.com/kwikteam/phy-data/zip/master -O phy-data.zip
unzip phy-data.zip
mkdir ./results

./build.sh

docker run -ti --rm -u $(id -u):$(id -g) -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -v $PWD/phy-data-master:/phy-data-master -v $PWD/results:/results geffenlab/ecephys-phy-desktop:local

conda_run python /opt/code/run_phy.py --data-root /phy-data-master/ --phy-pattern template/
```

```
ANALYSIS_ROOT=/home/ninjaben/codin/geffen-lab-data/analysis
SUBJECT=AS20-minimal
DATE=03112025

export ANALYSIS_PATH="$ANALYSIS_ROOT/$SUBJECT/$DATE"

docker run -ti --rm -u $(id -u):$(id -g) -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -v $ANALYSIS_PATH:/analysis geffenlab/geffenlab-phy-desktop:local conda_run python /opt/code/run_phy.py --data-root /analysis/exported --results-root /analysis/curated
```

```
./nextflow-25.04.6-dist -C geffenlab-phy-desktop/pipeline/main.config run geffenlab-phy-desktop/pipeline/main.nf
```