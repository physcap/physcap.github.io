# Code block 0
print("THOUGHT: I need to determine the physical properties (mass and stiffness) of the items to decide which should go into the bag first. Heavier and stiffer items should be placed at the bottom. I will start by checking the left-most red cube. | ACTION: Check left-most red cube")

red_mass = get_mass("left-most red cube")
red_stiffness = get_stiffness("left-most red cube")

print(f"Checked left-most red cube: mass = {red_mass} kg, stiffness = {red_stiffness}")

# Code block 1
print("THOUGHT: I have checked the red cube. Now I will check the physical properties of the yellow cube. | ACTION: Check yellow cube")

yellow_mass = get_mass("yellow cube")
yellow_stiffness = get_stiffness("yellow cube")

print(f"Checked yellow cube: mass = {yellow_mass} kg, stiffness = {yellow_stiffness}")

# Code block 2
print("THOUGHT: I have checked the yellow cube. Now I will check the physical properties of the green cube to see if it should go into the bag first. | ACTION: Check green cube")

green_mass = get_mass("green cube")
green_stiffness = get_stiffness("green cube")

print(f"Checked green cube: mass = {green_mass} kg, stiffness = {green_stiffness}")

# Code block 3
print("THOUGHT: I have checked the green cube. Now I will check the physical properties of the blue cube to see if it should go into the bag first. | ACTION: Check blue cube")
blue_mass = get_mass("right-most blue cube")
blue_stiffness = get_stiffness("right-most blue cube")
print(f"Checked right-most blue cube: mass = {blue_mass} kg, stiffness = {blue_stiffness}")
breakpoint_code_block()

# Code block 4
import numpy as np

print("THOUGHT: Based on the physical properties measured in the previous steps, the left-most red cube is the heaviest/stiffest and should form the base in the bag. | ACTION: Place left-most red cube in paper bag")
print("FIRST ITEM: left-most red cube")

# Locate the red cube
cube_pos, cube_quat = get_object_pose("left-most red cube")

# Grasp the red cube
open_gripper()
goto_pose(cube_pos, cube_quat, z_approach=0.1)
goto_pose(cube_pos, cube_quat)
close_gripper()
goto_pose(cube_pos, cube_quat, z_approach=0.1)

# Locate the bag and determine drop position
bag_pos, bag_quat = get_object_pose("paper grocery bag")
# Set a safe drop height (e.g., 0.25m) to clear the bag's rim
drop_pos = np.array([bag_pos[0], bag_pos[1], 0.25])

# Move to the bag and drop the cube
goto_pose(drop_pos, cube_quat)
open_gripper()

# Move 10 cm above the bag before going to home pose to avoid dragging
safe_pos = drop_pos + np.array([0.0, 0.0, 0.1])
goto_pose(safe_pos, cube_quat)

# Return to home pose
home_pose()