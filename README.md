# wbk Industrial Assembly Task Board

![Industrial Assembly Task Board Logo](docs/source/images/logo_with_text.png)

The **wbk Industrial Assembly Task Board** is a modular robotic benchmark developed by the wbk Institute of Production Science at KIT. This repository provides everything needed to build the hardware and evaluate robotic systems on a range of realistic assembly tasks.

You can find the full documentation and explanations of the tasks in the [documentation](https://industrial-assembly-taskboard.readthedocs.io/en/latest/).

## Why This Task Board?

Robotic assembly is more complex than simple "peg-in-hole" tasks. This task board introduces challenges like precise tolerances, compliant assembly, and advanced planning—reflecting real industrial scenarios. Its modular design lets you mix and match tasks to suit your research needs.

All 3D-printable files are available in the folder 3d_printing_files.

> **Note:** This is a starting point for exploring industrial assembly challenges. Contributions for new modules and tasks are welcome!

## Quick Start

1. Build the base task board and desired modules (see `wbk_challenge_overview`).
2. Review task definitions and evaluation metrics (`wbk_challenge_robot_tasks_overview`).
3. Implement your robot program, run experiments, and compare results.


![Sample Task Boards](docs/source/images/sample_taskboards.png)


# Citation
If you use this task board in your research, please cite our paper:
```bibtex
@misc{https://www.radar-service.eu/radar/en/dataset/3c5yh8z8asafagby.,
	doi = {10.35097/3c5yh8z8asafagby},
	author = {Baumgärtner, Jan and Kreft, Laurin and Puchta, Alexander and Fleischer, Jürgen},
	keywords = {Robotic Assembly and Industrial Automation and Peg-in-Hole and Pick-and-Place and Gear Assembly and Robotics and Industrial Robotics},
	title = {From Toy Problems to Industrial Reality: The wbk Assembly Benchmark},
	publisher = {Karlsruhe Institute of Technology},
	year = {2025}
}
```