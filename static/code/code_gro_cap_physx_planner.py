# Code block 0
print("THOUGHT: To determine a sensible packing order, I need to know the properties of the objects. I will start by measuring the mass of the red cube to see how heavy it is. | ACTION: measure_mass on cube_0")
mass = get_mass("the red cube on the far left")
print(f"Mass of cube_0: {mass}")
breakpoint_code_block()

# Code block 1
print("THOUGHT: I should measure the stiffness of the red cube on the far left to check if it's rigid or soft. | ACTION: measure_stiffness on cube_0")
stiffness = get_stiffness("the red cube on the far left")
print(f"Stiffness of cube_0: {stiffness}")
breakpoint_code_block()

# Code block 2
print("THOUGHT: Now I will measure the mass of the yellow cube second from the left to continue gathering information about the objects for my packing plan. | ACTION: measure_mass on cube_1")
mass_1 = get_mass("the yellow cube second from the left")
print(f"Mass of cube_1: {mass_1}")
breakpoint_code_block()

# Code block 3
print("THOUGHT: Now I will measure the stiffness of the yellow cube second from the left to check if it's rigid or soft. | ACTION: measure_stiffness on cube_1")
stiffness_1 = get_stiffness("the yellow cube second from the left")
print(f"Stiffness of cube_1: {stiffness_1}")
breakpoint_code_block()

# Code block 4
print("THOUGHT: Now I will measure the mass of the green cube second from the right to continue gathering information about the objects for my packing plan. | ACTION: measure_mass on cube_2")
mass_2 = get_mass("the green cube second from the right")
print(f"Mass of cube_2: {mass_2}")
breakpoint_code_block()

# Code block 5
print("THOUGHT: Now I will measure the stiffness of the green cube second from the right to check if it's rigid or soft. | ACTION: measure_stiffness on cube_2")
stiffness_2 = get_stiffness("the green cube second from the right")
print(f"Stiffness of cube_2: {stiffness_2}")
breakpoint_code_block()

# Code block 6
print("THOUGHT: Now I will measure the mass of the blue cube on the far right to complete gathering mass information about the objects for my packing plan. | ACTION: measure_mass on cube_3")
mass_3 = get_mass("the blue cube on the far right")
print(f"Mass of cube_3: {mass_3}")
breakpoint_code_block()

# Code block 7
print("THOUGHT: Now I will measure the stiffness of the blue cube on the far right to complete gathering information about the objects for my packing plan. | ACTION: measure_stiffness on cube_3")
stiffness_3 = get_stiffness("the blue cube on the far right")
print(f"Stiffness of cube_3: {stiffness_3}")
breakpoint_code_block()

# Code block 8
import numpy as np

print("THOUGHT: The green cube is the heaviest (0.476 kg) and is rigid (level 5), making it the ideal first item to place at the bottom of the bag. | ACTION: Pick up cube_2 and place it in bag_0.")
print("FIRST ITEM: cube_2")

cube_2_pos, _ = get_object_pose("the green cube second from the right")
bag_pos, _ = get_object_pose("the white bag in the center")

# Pick up the green cube
open_gripper()
goto_pose(cube_2_pos, z_approach=0.1)
close_gripper()

# Lift the cube
goto_pose(cube_2_pos + np.array([0, 0, 0.1]))

# Move to the bag and drop it
drop_pos = bag_pos + np.array([0.0, 0.0, 0.05])
goto_pose(drop_pos, z_approach=0.1)
open_gripper()

# Move 10 cm above the bag before going home
goto_pose(bag_pos + np.array([0.0, 0.0, 0.1]))

# Return to home pose
home_pose()