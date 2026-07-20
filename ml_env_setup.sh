#!/bin/bash
# This script injects the Pixi-downloaded PyPI CUDA libraries into the environment path
# so that the Jetson PyTorch wheel can find them without modifying the host machine.
export LD_LIBRARY_PATH=$PIXI_PROJECT_ROOT/.pixi/envs/ml/lib/python3.10/site-packages/nvidia/cu12/lib:$PIXI_PROJECT_ROOT/.pixi/envs/ml/lib/python3.10/site-packages/nvidia/cusparselt/lib:$LD_LIBRARY_PATH
