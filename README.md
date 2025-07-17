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

conda_run python /opt/code/run.py --data-root /phy-data-master/ --phy-pattern template/
```

```
ANALYSIS_ROOT=/home/ninjaben/codin/geffen-lab-data/analysis
SUBJECT=AS20-minimal
DATE=03112025
EXPORTED_PATH="$ANALYSIS_ROOT/$SUBJECT/$DATE/exported"
RESULTS_PATH="$ANALYSIS_ROOT/$SUBJECT/$DATE/curated"
mkdir -p "$RESULTS_PATH"

docker run -ti --rm -u $(id -u):$(id -g) -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -v $EXPORTED_PATH:/data -v $RESULTS_PATH:/results geffenlab/ecephys-phy-desktop:local

conda_run python /opt/code/run.py
```
