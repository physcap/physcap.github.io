# Code block 0
import numpy as np

print("THOUGHT: To find the blue cubes, I will lift the left brown paper cup to check if a blue cube is underneath it. | ACTION: Lift left brown paper cup")

cup_pos, cup_quat = get_object_pose("left brown paper cup")
tray_pos, tray_quat = get_object_pose("wooden tray")

# Grasp the cup
open_gripper()
goto_pose(cup_pos, cup_quat, z_approach=0.1)
close_gripper()

# Lift the cup
goto_pose(cup_pos + np.array([0, 0, 0.1]), cup_quat)

# Calculate place position over the tray
place_pos = tray_pos.copy()
place_pos[2] = cup_pos[2] + 0.05

# Move to the tray and place
goto_pose(place_pos, tray_quat, z_approach=0.1)
open_gripper()

# Retreat
goto_pose(place_pos + np.array([0, 0, 0.1]), tray_quat)

# Return home
home_pose()
breakpoint_code_block()

# Code block 1
import numpy as np

print("THOUGHT: I will lift the right brown paper cup to check if another blue cube is hidden underneath it. | ACTION: Lift right brown paper cup")

cup_pos, cup_quat = get_object_pose("right brown paper cup")
tray_pos, tray_quat = get_object_pose("wooden tray")

# Grasp the cup
open_gripper()
goto_pose(cup_pos, cup_quat, z_approach=0.1)
close_gripper()

# Lift the cup
goto_pose(cup_pos + np.array([0, 0, 0.1]), cup_quat)

# Calculate place position over the tray
place_pos = tray_pos.copy()
place_pos[2] = cup_pos[2] + 0.05

# Move to the tray and place
goto_pose(place_pos, tray_quat, z_approach=0.1)
open_gripper()

# Retreat
goto_pose(place_pos + np.array([0, 0, 0.1]), tray_quat)

# Return home
home_pose()
breakpoint_code_block()

# Code block 2
print("THOUGHT: The third blue cube was revealed after lifting the right brown paper cup, meaning all three blue cubes are now in sight. The objective is achieved so the task is complete. | ACTION: None")