# Code block 0
mass = get_mass("the red cube on the left")
print(f"Mass of cube_0 (the red cube on the left): {mass} kg")
breakpoint_code_block()

# Code block 1
mass = get_mass("the yellow cube second from the left")
print(f"Mass of cube_1 (the yellow cube second from the left): {mass} kg")
breakpoint_code_block()

# Code block 2
mass = get_mass("the green cube second from the right")
print(f"Mass of cube_2 (the green cube second from the right): {mass} kg")
breakpoint_code_block()

# Code block 3
mass = get_mass("the blue cube on the right")
print(f"Mass of cube_3 (the blue cube on the right): {mass} kg")
breakpoint_code_block()

# Code block 4
stiffness = get_stiffness("the yellow cube second from the left")
print(f"Stiffness of cube_1 (the yellow cube second from the left): {stiffness}")
breakpoint_code_block()

# Code block 5
stiffness = get_stiffness("the green cube second from the right")
print(f"Stiffness of cube_2 (the green cube second from the right): {stiffness}")
breakpoint_code_block()

# Code block 6
import numpy as np

print("THOUGHT: The green cube is heavy (0.356 kg) and completely rigid (stiffness level 5). To prevent crushing softer items like the semi-rigid yellow cube, the most rigid and heavy items should be packed at the very bottom of the bag. | ACTION: Pack cube_2 into bag_0.")
print("FIRST ITEM: cube_2")

cube_pos, cube_quat = get_object_pose("the green cube second from the right")
bag_pos, bag_quat = get_object_pose("the white paper bag in the middle")

open_gripper()

# Move 10 cm above the cube before grasping to avoid collisions
goto_pose(cube_pos, z_approach=0.1)
goto_pose(cube_pos)
close_gripper()

# Lift the cube 10 cm above its original position
goto_pose(cube_pos, z_approach=0.1)

# Move to the bag, aiming 5 cm above the bag's rim to ensure it clears the wall
drop_pos = bag_pos.copy()
drop_pos[2] = max(drop_pos[2] + 0.20, 0.25) # approximate rim height + 5cm
goto_pose(drop_pos)
open_gripper()

# Move 10 cm above the bag after placing the item
post_drop_pos = drop_pos.copy()
post_drop_pos[2] += 0.10
goto_pose(post_drop_pos)

# Return to home pose
home_pose()