#!/bin/sh

set -e

docker build -f environment/Dockerfile -t geffenlab/geffenlab-phy-desktop:local .
