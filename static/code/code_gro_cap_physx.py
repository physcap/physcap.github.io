# Code block 0
print("THOUGHT: I need to evaluate the physical properties of the items to determine a sensible packing order. The heaviest and stiffest item should be placed at the bottom of the bag. I will measure the items one by one. I will start with the red cube on the far left. | ACTION: Measure red cube on the far left")

mass = get_mass("red cube on the far left")
stiffness = get_stiffness("red cube on the far left")

print(f"Checked: red cube on the far left - Mass: {mass} kg, Stiffness: {stiffness}")
print("Unchecked: yellow cube on the center left, green cube on the center right, blue cube on the far right")

# Code block 1
print("THOUGHT: I have measured the red cube. Now I will measure the yellow cube on the center left to compare its physical properties. | ACTION: Measure yellow cube on the center left")

mass = get_mass("yellow cube on the center left")
stiffness = get_stiffness("yellow cube on the center left")

print(f"Checked: red cube (M: 0.044kg, S: 3), yellow cube (M: {mass:.3f}kg, S: {stiffness})")
print("Unchecked: green cube on the center right, blue cube on the far right")

# Code block 2
print("THOUGHT: I have measured the red and yellow cubes. Now I will measure the green cube on the center right to determine its physical properties. | ACTION: Measure green cube on the center right")

mass = get_mass("green cube on the center right")
stiffness = get_stiffness("green cube on the center right")

print(f"Checked: red cube (M: 0.044kg, S: 3), yellow cube (M: 0.430kg, S: 3), green cube (M: {mass:.3f}kg, S: {stiffness})")
print("Unchecked: blue cube on the far right")

# Code block 3
print("THOUGHT: I have measured the red, yellow, and green cubes. Now I will measure the blue cube on the far right to complete my assessment of all items before deciding which one should go into the bag first. | ACTION: Measure blue cube on the far right")

mass = get_mass("blue cube on the far right")
stiffness = get_stiffness("blue cube on the far right")

print(f"Checked: red cube (M: 0.044kg, S: 3), yellow cube (M: 0.430kg, S: 3), green cube (M: 0.429kg, S: 5), blue cube (M: {mass:.3f}kg, S: {stiffness})")
print("Unchecked: None")

# Code block 4
print("THOUGHT: Now I have the properties of all cubes. The green cube is both heavy (0.429 kg) and the most rigid (stiffness 5). Placing the heaviest and most rigid item at the bottom of the bag provides a stable base for the rest of the groceries. I will place the green cube in the bag first. | ACTION: Place green cube on the center right into the bag")
print("FIRST ITEM: green cube on the center right")

open_gripper()

# Pick up the green cube
cube_pos, _ = get_object_pose("green cube on the center right")
goto_pose(cube_pos, z_approach=0.1)
goto_pose(cube_pos)
close_gripper()

# Go to the paper bag opening
bag_pos, _ = get_object_pose("paper bag opening")

# Aim for 5 cm above the bag's rim before opening the gripper
drop_pos = bag_pos.copy()
drop_pos[2] += 0.05
goto_pose(drop_pos)
open_gripper()

# Move 10 cm above the bag before going to home pose
retreat_pos = drop_pos.copy()
retreat_pos[2] += 0.1
goto_pose(retreat_pos)

home_pose()