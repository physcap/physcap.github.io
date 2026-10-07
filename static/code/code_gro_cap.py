# Code block 0
print("THOUGHT: The yellow cube is on the left and easily accessible. I will pick it up and place it in the bag. | ACTION: yellow cube")
print("FIRST ITEM: yellow cube")

import numpy as np

# Get poses
cube_pos, cube_quat = get_object_pose("yellow cube")
bag_pos, bag_quat = get_object_pose("paper bag")

# Open gripper to prepare for grasping
open_gripper()

# Move 10 cm above the object before going to target
goto_pose(cube_pos, cube_quat, z_approach=0.1)

# Close gripper to grab the cube
close_gripper()

# Lift the cube 10 cm above its original position
hover_cube_pos = cube_pos.copy()
hover_cube_pos[2] += 0.1
goto_pose(hover_cube_pos, cube_quat)

# Move to the bag, aiming for 5 cm above the bag's rim
# The bag's rim is typically higher than its center coordinate
bag_release_pos = bag_pos.copy()
bag_release_pos[2] += 0.15  # Adjusting roughly for bag height + 5cm clearance
goto_pose(bag_release_pos, bag_quat)

# Drop the cube
open_gripper()

# Move 10 cm above the bag to avoid dragging it
bag_hover_pos = bag_release_pos.copy()
bag_hover_pos[2] += 0.1
goto_pose(bag_hover_pos, bag_quat)

# Go home
home_pose()