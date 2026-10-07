# Code block 0
print("THOUGHT: I will measure the mass of the black can on the far left to check if it is the empty one. | ACTION: Lift can_0")
mass = get_mass("the black can on the far left")
print(f"Mass of can_0: {mass} kg")
breakpoint_code_block()

# Code block 1


# Code block 2
print("THOUGHT: I will measure the mass of the blue can second from the right to check if it is the empty one. | ACTION: Lift can_2")
mass = get_mass("the blue can second from the right")
print(f"Mass of can_2: {mass} kg")
breakpoint_code_block()

# Code block 3
print("THOUGHT: I will measure the mass of the red Coca-Cola can on the far right to check if it is the empty one. | ACTION: Lift can_3")
mass = get_mass("the red Coca-Cola can on the far right")
print(f"Mass of can_3: {mass} kg")
breakpoint_code_block()

# Code block 4
import numpy as np

print("THOUGHT: The red Coca-Cola can on the far right (can_3) was measured to have a mass of -0.0376 kg. Since this is below 0.1 kg, it is the empty can. I will pick it up and place it on the wooden tray to complete the task. | ACTION: Lift can_3")
print("Empty can confirmed: can_3")

can_pos, can_quat = get_object_pose("the red Coca-Cola can on the far right")
tray_pos, tray_quat = get_object_pose("the wooden tray in the middle")

# Open gripper and approach the empty can
open_gripper()
goto_pose(can_pos, can_quat, z_approach=0.1)

# Grasp the can
goto_pose(can_pos, can_quat)
close_gripper()

# Lift 10 cm above the object to avoid collisions before moving laterally
goto_pose(can_pos + np.array([0.0, 0.0, 0.1]), can_quat)

# Move to the tray, matching object's original grasp z-coordinate + 5 cm to clear the tray's lip safely
place_pos = np.array([tray_pos[0], tray_pos[1], can_pos[2] + 0.05])
goto_pose(place_pos, can_quat)

# Release the can onto the tray
open_gripper()

# Lift arm 20 cm above the tray and object before going home
goto_pose(place_pos + np.array([0.0, 0.0, 0.2]), can_quat)

# Task complete, return to home position
home_pose()