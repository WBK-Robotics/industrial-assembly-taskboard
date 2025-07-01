Task Descriptions
=================


This section describes all tasks of the industrial assembly task board.
Like the assembly instructions, the individual tasks are organized in modules but can be mixed and matched freely to create custom benchmarks.

How to use this guide
---------------------

1. Pick the tasks you want to benchmark.
2. Read its **robotic assembly task** page to understand the required motions and tolerances.
3. Implement and test your robot program until the success criteria are met.

Module Overview
----------------

Each module is designed to test specific aspects of robotic assembly, focusing on challenges commonly encountered in industrial practice. Below is a detailed description of each module and the reasoning behind its design:

Peg in Hole Tasks
^^^^^^^^^^^^^^^^^

While peg-in-hole is a classic benchmark in academic robotics, real industrial assembly often involves much tighter tolerances and more complex geometries. 
This module includes tasks with round shafts, splined shafts, and connectors, requiring precise alignment and insertion. 
These tasks test the robot’s ability to handle realistic industrial fits, going beyond the simplified versions often seen in research.

Pick and Place Tasks
^^^^^^^^^^^^^^^^^^^^

Industrial pick-and-place is rarely just about moving objects from one location to another. 
Components may vary in size, shape, or orientation, and often require adaptive alignment relative to each other or iterative adjustments to meet specific tolerances. 
This module introduces such variability, challenging the robot to adapt its strategy and ensure accurate placement.

Gear Assembly Tasks
^^^^^^^^^^^^^^^^^^^

Assembling gears in industry requires careful alignment, meshing, and sometimes coordination of multiple moving parts. 
For keyed gears this might even involve some planning to first align the keyways before inserting the gear.
The tasks in this module involve spur and helical gears, as well as multi-gear setups, 
testing the robot’s ability to plan and execute complex assemblies that mirror actual industrial challenges.

Screws and Nuts Tasks
^^^^^^^^^^^^^^^^^^^^^

In practice, screwing and fastening often occur in constrained or awkward spaces, not just on open, accessible surfaces. 
This module presents tasks with tilted screws and limited accessibility, requiring dexterous manipulation and problem-solving. 
These scenarios simulate the real difficulties robots face when assembling products in tight or obstructed environments.

Elastic Deformation Tasks
^^^^^^^^^^^^^^^^^^^^^^^^^

Many industrial assemblies involve parts that must be flexed, snapped, or compressed into place, such as springs or circlips. 
Unlike rigid part handling, these tasks require the robot to control force and deformation.
This module tests the robot’s ability to manage non-rigid components common in real world connectors such as snaps, clips, and springs.

Assembly Task
-------------

.. toctree::
   :maxdepth: 1
   :caption: Robot Tasks

   robotic_instructions_peg_in_hole
   robotic_instructions_pick_and_place
   robotic_instructions_gear_tasks
   robotic_instructions_screws_and_nuts
   robotic_instructions_elastic_deformation
