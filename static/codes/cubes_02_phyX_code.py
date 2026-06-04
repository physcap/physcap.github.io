# Code block 0
import numpy as np

print('THOUGHT: There are only two blue cubes visible on the table. The third one must be hidden. Since paper cups are large enough to cover a blue cube, I will systematically lift them to find the hidden one. I will start by lifting the left-most tan paper cup. | ACTION: Lift left-most tan paper cup')

# Get poses for the target cup and the wooden tray
cup_pos, cup_quat = get_object_pose("left-most tan paper cup")
tray_pos, tray_quat = get_object_pose("wooden tray")

# Move to and grasp the cup
open_gripper()
goto_pose(cup_pos, z_approach=0.10)
close_gripper()

# Lift the cup
goto_pose(cup_pos + np.array([0.0, 0.0, 0.10]))

# Calculate place position over the wooden tray (match object's height + 5cm)
place_pos = np.array([tray_pos[0], tray_pos[1], cup_pos[2] + 0.05])

# Move to the tray and place the cup
goto_pose(place_pos, z_approach=0.10)
open_gripper()

# Move up to avoid collisions, then return to home pose
goto_pose(place_pos + np.array([0.0, 0.0, 0.10]))
home_pose()

breakpoint_code_block()

# Code block 1
import numpy as np

print('THOUGHT: Did not find any new blue cubes under the previous cup. There are still only two blue cubes visible. I will lift the white paper cup to check if the third blue cube is underneath it. | ACTION: Lift white paper cup')

# Get poses for the target cup and the wooden tray
cup_pos, cup_quat = get_object_pose("white paper cup")
tray_pos, tray_quat = get_object_pose("wooden tray")

# Move to and grasp the cup
open_gripper()
goto_pose(cup_pos, z_approach=0.10)
close_gripper()

# Lift the cup
goto_pose(cup_pos + np.array([0.0, 0.0, 0.10]))

# Calculate place position over the wooden tray (match object's height + 5cm)
place_pos = np.array([tray_pos[0], tray_pos[1], cup_pos[2] + 0.05])

# Move to the tray and place the cup
goto_pose(place_pos, z_approach=0.10)
open_gripper()

# Move up to avoid collisions, then return to home pose
goto_pose(place_pos + np.array([0.0, 0.0, 0.10]))
home_pose()

breakpoint_code_block()

# Code block 2
import numpy as np

print('THOUGHT: Did not find any new blue cubes under the white paper cup. There are still only two blue cubes visible. I will lift the remaining tan paper cup to find the third blue cube. | ACTION: Lift tan paper cup')

# Get poses for the target cup and the wooden tray
cup_pos, cup_quat = get_object_pose("tan paper cup")
tray_pos, tray_quat = get_object_pose("wooden tray")

# Move to and grasp the cup
open_gripper()
goto_pose(cup_pos, z_approach=0.10)
close_gripper()

# Lift the cup
goto_pose(cup_pos + np.array([0.0, 0.0, 0.10]))

# Calculate place position over the wooden tray (match object's height + 5cm)
place_pos = np.array([tray_pos[0], tray_pos[1], cup_pos[2] + 0.05])

# Move to the tray and place the cup
goto_pose(place_pos, z_approach=0.10)
open_gripper()

# Move up to avoid collisions, then return to home pose
goto_pose(place_pos + np.array([0.0, 0.0, 0.10]))
home_pose()

breakpoint_code_block()