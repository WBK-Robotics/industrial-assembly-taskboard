Robotic Assembly Instructions: Pick and Place
=============================================

Task 1: Housing Parts
---------------------

Task Description:
-----------------

The first housing part is firmly screwed onto the Taskboard, while the second housing part lies on a flat surface next to the board.
First the robot must grasp the housing part laying next to the Taskboard.
Then the robot must position it centrally above the first housing part mounted on the Taskboard and place it down.
In doing so, the robot must ensure that the holes provided - symbolizing screw connections - are congruent on both housing parts. The assembly can only be considered successful if this fit is ensured.
Success criteria: The housing part must be placed on top of the component fixed to the Taskboard, ensuring parallel alignment. The distance between the two flange surfaces must be exactly 2 mm; otherwise, the part is not correctly centered.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Additionally, the center axes of the aligned drill holes must match, with a maximum allowable rotational deviation of 1° from the housing parts’ central axis.
If both conditions are met, the assembly is considered successful.

Task 2: Feather Key
-------------------

Task Description:
-----------------

The shaft is firmly screwed onto the task board, while the feather key lies on a flat surface next to the board.
The robot grasps the feather key and brings it into position for inserting it into the groove on the shaft.
The robot then lowers the feather key vertically into the groove, while considering that the key can’t be grasped over its complete height and inserted at the same time.

Success criteria: The robot must fully insert the feather key into the groove on the assembly component on the Taskboard without dropping it, ensuring that there is no vertical movement once the robot releases its grip. If this condition is met, the assembly is considered successful.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Task 3: Shim Ring
-----------------

Task Description:
-----------------

The shaft on which the shims are to be mounted later by the robot is firmly screwed to the task board. The magazine containing the shim rings is placed on a flat surface next to the task board.
The robot first picks a shim ring out of the magazine.
Then the robot must align and place the shim ring on the assembly shaft mounted on the Task board.

The robot must repeat these actions and stack the shim rings until the placement of another shim ring, would obstructs the visibility of the groove in the assembly component after a theoretical placement. Once this stage is reached the task is completed successfully.
Success criteria: The robot must place 4 out of the 5 provided shim rings onto the shaft of the assembly component, so that the stacked shim rings then reach the groove that marks the target height without covering it. The required number must be determined autonomously by the robot and should not be predefined.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If these conditions are met, the assembly is considered successful.
