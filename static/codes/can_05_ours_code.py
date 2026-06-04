# Code block 0
import numpy as np

print("THOUGHT: Checking the weight of the second from left green can to see if it is the empty one. | ACTION: Lift second from left green can")
weight = get_weight("second from left green can")
print(f"Weight of second from left green can: {weight}")

if weight < 0.1:
    print("Empty can confirmed: second from left green can")
    
    can_pos, can_quat = get_object_pose("second from left green can")
    tray_pos, tray_quat = get_object_pose("wooden tray")
    
    open_gripper()
    goto_pose(can_pos, can_quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object to avoid collisions
    approach_pos = can_pos.copy()
    approach_pos[2] += 0.1
    goto_pose(approach_pos, can_quat)
    
    # Calculate target position for placing
    target_pos = tray_pos.copy()
    target_pos[2] = can_pos[2] + 0.05
    
    # Move 10 cm above target
    target_approach = target_pos.copy()
    target_approach[2] += 0.1
    goto_pose(target_approach, can_quat)
    
    # Place on tray
    goto_pose(target_pos, can_quat)
    open_gripper()
    
    # Move above tray and object before going to home pose
    goto_pose(target_approach, can_quat)
    home_pose()
else:
    print("can second from left green can is not empty.")
    breakpoint_code_block()

# Code block 1
import numpy as np

print("THOUGHT: Checking the weight of the right-most red can to see if it is the empty one. | ACTION: Lift right-most red can")
weight = get_weight("right-most red can")
print(f"Weight of right-most red can: {weight}")

if weight < 0.1:
    print("Empty can confirmed: right-most red can")
    
    can_pos, can_quat = get_object_pose("right-most red can")
    tray_pos, tray_quat = get_object_pose("wooden tray")
    
    open_gripper()
    goto_pose(can_pos, can_quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object to avoid collisions
    approach_pos = can_pos.copy()
    approach_pos[2] += 0.1
    goto_pose(approach_pos, can_quat)
    
    # Calculate target position for placing
    target_pos = tray_pos.copy()
    target_pos[2] = can_pos[2] + 0.05
    
    # Move 10 cm above target
    target_approach = target_pos.copy()
    target_approach[2] += 0.1
    goto_pose(target_approach, can_quat)
    
    # Place on tray
    goto_pose(target_pos, can_quat)
    open_gripper()
    
    # Move above tray and object before going to home pose
    goto_pose(target_approach, can_quat)
    home_pose()
else:
    print("can right-most red can is not empty.")
    breakpoint_code_block()

# Code block 2
import numpy as np

print("THOUGHT: The empty can (right-most red can) has already been successfully identified and relocated to the wooden tray in the previous step. The task is fully complete and no further actions are necessary. | ACTION: End task")
home_pose()