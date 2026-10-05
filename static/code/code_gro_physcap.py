# Code block 0
print("THOUGHT: I need to measure the mass of the red cube on the far left to determine its properties for packing order. Heavy and rigid items should be packed first at the bottom of the bag. | ACTION: Measure mass of cube_0")
mass = get_mass("the red cube on the far left")
print(f"Mass of cube_0: {mass:.3f} kg")
breakpoint_code_block()

# Code block 1
print("THOUGHT: I need to measure the mass of the yellow cube to help determine the packing order. | ACTION: Measure mass of cube_1")
mass_1 = get_mass("the yellow cube second from the left")
print(f"Mass of cube_1: {mass_1:.3f} kg")
breakpoint_code_block()

# Code block 2
print("THOUGHT: I need to measure the mass of the green cube to help determine the packing order. | ACTION: Measure mass of cube_2")
mass_2 = get_mass("the green cube second from the right")
print(f"Mass of cube_2: {mass_2:.3f} kg")
breakpoint_code_block()

# Code block 3
print("THOUGHT: I need to measure the mass of the blue cube to help determine the packing order. | ACTION: Measure mass of cube_3")
mass_3 = get_mass("the blue cube on the far right")
print(f"Mass of cube_3: {mass_3:.3f} kg")
breakpoint_code_block()

# Code block 4
print("THOUGHT: I need to measure the stiffness of the yellow cube to help determine if it should be packed at the bottom or top of the bag. | ACTION: Measure stiffness of cube_1")
stiffness_1 = get_stiffness("the yellow cube second from the left")
print(f"Stiffness of cube_1: {stiffness_1}")
breakpoint_code_block()

# Code block 5
print("THOUGHT: I need to measure the stiffness of the green cube to help determine if it should be packed at the bottom or top of the bag. | ACTION: Measure stiffness of cube_2")
stiffness_2 = get_stiffness("the green cube second from the right")
print(f"Stiffness of cube_2: {stiffness_2}")
breakpoint_code_block()

# Code block 6
import numpy as np

print("THOUGHT: Based on the measurements, the green cube is the heaviest (0.411 kg) and most rigid (level 5), making it the ideal foundational item for the bottom of the bag. | ACTION: Pack cube_2")
print("FIRST ITEM: cube_2")

# Get cube pose
cube_pos, cube_quat = get_object_pose("the green cube second from the right")

# Approach and grasp the green cube
open_gripper()
goto_pose(cube_pos, z_approach=0.1)
goto_pose(cube_pos)
close_gripper()
goto_pose(cube_pos, z_approach=0.1)

# Get bag pose
bag_pos, bag_quat = get_object_pose("the white paper bag in the middle")

# Aim for 5 cm above the bag's rim. 
# We add an offset to the bag's detected Z position to safely clear the rim.
drop_pos = bag_pos.copy()
drop_pos[2] += 0.15

# Approach the drop position (z_approach adds another 10 cm initially)
goto_pose(drop_pos, z_approach=0.1)

# Move down to exactly 5 cm above the bag's rim
goto_pose(drop_pos)

# Release the cube into the bag
open_gripper()

# Move 10 cm above the bag drop position before going home to avoid dragging it
goto_pose(drop_pos, z_approach=0.1)

# Return to rest pose
home_pose()
