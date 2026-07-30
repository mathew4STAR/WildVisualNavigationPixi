#!/bin/bash
# Removes sim python 3.12 site-packages from PYTHONPATH to avoid conflicting
# with the ml environment's Python 3.10 site-packages when loading numpy, etc.

# Forcefully construct a clean PYTHONPATH. Order matters!
# 1. ml environment (so its numpy/pytorch takes precedence over sim env's)
# 2. devel space (for custom msgs like wild_visual_navigation_msgs, and symlinked ROS python packages)
export PYTHONPATH="/home/airlagx1/elevation_tests/wvn_git/.pixi/envs/ml/lib/python3.10/site-packages:/home/airlagx1/elevation_tests/wvn_git/devel/lib/python3.12/site-packages"

# Forcefully construct a clean LD_LIBRARY_PATH containing ONLY the ml env and devel space
export LD_LIBRARY_PATH="/home/airlagx1/elevation_tests/wvn_git/.pixi/envs/ml/lib:/home/airlagx1/elevation_tests/wvn_git/devel/lib:/home/airlagx1/elevation_tests/wvn_git/.pixi/envs/ml/lib/python3.10/site-packages/nvidia/cu12/lib:/home/airlagx1/elevation_tests/wvn_git/.pixi/envs/ml/lib/python3.10/site-packages/nvidia/cusparselt/lib"

# Also unset ROS_DISTRO just in case any internal scripts check it
unset ROS_DISTRO

# Execute python directly from the ml environment to avoid pixi concurrent lock deadlocks
exec /home/airlagx1/elevation_tests/wvn_git/.pixi/envs/ml/bin/python "$@"
