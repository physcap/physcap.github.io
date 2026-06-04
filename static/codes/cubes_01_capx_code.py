# Code block 0
import numpy as np

print("THOUGHT: I can only see two blue cubes on the table. The third blue cube must be hidden under one of the cups. I will lift the brown cup on the left to check if it's there. | ACTION: Lift brown cup on the left.")

left_cup_pos, left_cup_quat = get_object_pose("brown cup on the left")
tray_pos, tray_quat = get_object_pose("wooden tray")

open_gripper()
goto_pose(left_cup_pos, left_cup_quat, z_approach=0.1)
close_gripper()

cup_lift_pos = left_cup_pos.copy()
cup_lift_pos[2] += 0.1
goto_pose(cup_lift_pos, left_cup_quat)

target_pos = tray_pos.copy()
target_pos[2] = left_cup_pos[2] + 0.05

goto_pose(target_pos, tray_quat, z_approach=0.1)
open_gripper()

target_lift_pos = target_pos.copy()
target_lift_pos[2] += 0.1
goto_pose(target_lift_pos, tray_quat)

home_pose()
breakpoint_code_block()

# Code block 1
import numpy as np

print("THOUGHT: Did not find any new blue cubes. The third blue cube must be hidden under the white cup or the brown cup. I will lift the white cup to check if it's there. | ACTION: Lift white cup.")

cup_pos, cup_quat = get_object_pose("white cup")
tray_pos, tray_quat = get_object_pose("wooden tray")

open_gripper()
# Approach and grasp the cup
goto_pose(cup_pos, cup_quat, z_approach=0.1)
close_gripper()

# Lift the cup
cup_lift_pos = cup_pos.copy()
cup_lift_pos[2] += 0.15
goto_pose(cup_lift_pos, cup_quat)

# Move to tray and place
target_pos = tray_pos.copy()
target_pos[2] = cup_pos[2] + 0.05

goto_pose(target_pos, tray_quat, z_approach=0.1)
open_gripper()

# Retreat from tray
target_lift_pos = target_pos.copy()
target_lift_pos[2] += 0.15
goto_pose(target_lift_pos, tray_quat)

home_pose()
breakpoint_code_block()

# Code block 2
import numpy as np

print("THOUGHT: Did not find any new blue cubes. I still only see two blue cubes on the table. The third blue cube must be hidden under the remaining brown cup. I will lift it to check. | ACTION: Lift brown cup.")

cup_pos, cup_quat = get_object_pose("brown cup")
tray_pos, tray_quat = get_object_pose("wooden tray")

open_gripper()
# Approach and grasp the cup
goto_pose(cup_pos, cup_quat, z_approach=0.1)
close_gripper()

# Lift the cup
cup_lift_pos = cup_pos.copy()
cup_lift_pos[2] += 0.15
goto_pose(cup_lift_pos, cup_quat)

# Move to tray and place
target_pos = tray_pos.copy()
target_pos[2] = cup_pos[2] + 0.05

goto_pose(target_pos, tray_quat, z_approach=0.1)
open_gripper()

# Retreat from tray
target_lift_pos = target_pos.copy()
target_lift_pos[2] += 0.15
goto_pose(target_lift_pos, tray_quat)

home_pose()
breakpoint_code_block()