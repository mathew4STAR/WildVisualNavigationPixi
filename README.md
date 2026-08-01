# Wild Visual Navigation (Pixi Port for Jetson Orin)

![Overview](./src/wild_visual_navigation/assets/drawings/header.jpg)

This package implements the Wild Visual Navigation (WVN) system presented in Frey & Mattamala et al. ["Fast Traversability Estimation for Wild Visual Navigation"](https://www.roboticsproceedings.org/rss19/p054.html) (2023) and later extended in Mattamala & Frey et al. ["Wild Visual Navigation: Fast Traversability Learning via Pre-Trained Models and Online Self-Supervision"](https://arxiv.org/abs/2404.07110) (2024). 

It provides a visual, self-supervised traversability estimation system for mobile robots, which trains dynamically online after just a few minutes of human demonstrations in the field.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mathew4STAR/WildVisualNavigationPixi
   cd wvn_git
   ```

2. **Install Environments via Pixi**
   This project uses [Pixi](https://pixi.sh) to strictly isolate the ROS Noetic environment (`sim`) from the PyTorch ML environment (`ml`).
   ```bash
   pixi install
   ```

## Running the System

To test the system and watch the robot learn, you will need to run two separate commands in two separate terminals.

1. **Launch the Simulation and WVN Stack**
   This single command launches the Gazebo simulation, RViz, the ROS bridge, and the PyTorch WVN neural networks.
   ```bash
   pixi run -e sim bash -c "source devel/setup.bash && roslaunch wvn_sim sim.launch"
   ```

2. **Drive the Robot (Teleop)**
   Open a second terminal to drive the robot around. As you drive into obstacles and the robot struggles to move, the WVN system will automatically calculate the velocity error and train the neural network to recognize those obstacles visually!
   ```bash
   pixi run -e sim bash -c "source devel/setup.bash && rosrun teleop_twist_keyboard teleop_twist_keyboard.py"
   ```

## Helpful Commands

**Rebuilding the Workspace**
If you modify any C++ files, world files, or launch files, you must rebuild the workspace:
```bash
pixi shell -e sim
catkin clean -y
catkin build -DPYTHON_EXECUTABLE=$PIXI_PROJECT_ROOT/.pixi/envs/sim/bin/python
exit
```

**Entering Interactive Shells**
If you need to interactively inspect the environments:
```bash
pixi shell -e sim  # Enter the ROS Noetic environment
pixi shell -e ml   # Enter the Python 3.10 PyTorch environment
```

**Sourcing the ROS Environment**
Any time you enter a `pixi shell -e sim` to use ROS commands, always remember to source the workspace:
```bash
source devel/setup.bash
```

---

<br>
<br>

> *Note: This repository is a Pixi-based port of the original Dockerized WVN repository. This port was created specifically to run natively on NVIDIA Jetson devices running Ubuntu 22.04 (JetPack 6). The original repository relied on an Ubuntu 20.04 Docker container, which caused fatal CUDA driver incompatibilities on JetPack 6 because Jetson container CUDA drivers are not backwards compatible across major OS releases.*
