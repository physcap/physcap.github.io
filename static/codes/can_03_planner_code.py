# Code block 0
print("THOUGHT: The objective is to identify the empty can by measuring their weights. We will begin with the leftmost blue can. | ACTION: Lift leftmost blue can")
weight = get_weight("leftmost blue can")
print(f"leftmost blue can weight: {weight}")
if weight < 0.1:
    print("Empty can confirmed: leftmost blue can")
else:
    print("can leftmost blue can is not empty.")
breakpoint_code_block()

# Code block 1
import numpy as np

print("THOUGHT: The leftmost blue can was not empty. I will now check the second from left can, which is green. | ACTION: Lift second from left green can")
weight = get_weight("second from left green can")
print(f"second from left green can weight: {weight}")

if weight < 0.1:
    print("Empty can confirmed: second from left green can")
    can_pos, can_quat = get_object_pose("second from left green can")
    tray_pos, _ = get_object_pose("wooden tray")
    
    open_gripper()
    # Move 10 cm above before grasping
    goto_pose(can_pos, can_quat, z_approach=0.1)
    goto_pose(can_pos, can_quat)
    close_gripper()
    
    # Move 10 cm above to avoid collisions before going to target
    lift_pos = can_pos.copy()
    lift_pos[2] += 0.1
    goto_pose(lift_pos, can_quat)
    
    # Target height is object's z-coord + 5cm as instructed
    target_pos = tray_pos.copy()
    target_pos[2] = can_pos[2] + 0.05
    
    # Move to tray and place
    goto_pose(target_pos, can_quat, z_approach=0.1)
    goto_pose(target_pos, can_quat)
    open_gripper()
    
    # Move 10 cm above tray before returning home
    post_place_pos = target_pos.copy()
    post_place_pos[2] += 0.1
    goto_pose(post_place_pos, can_quat)
    
    home_pose()
else:
    print("can second from left green can is not empty.")
    breakpoint_code_block()

# Code block 2
import numpy as np

print("THOUGHT: The green can was not empty. I will now check the second from right black can. | ACTION: Lift second from right black can")
weight = get_weight("second from right black can")
print(f"second from right black can weight: {weight}")

if weight < 0.1:
    print("Empty can confirmed: second from right black can")
    can_pos, can_quat = get_object_pose("second from right black can")
    tray_pos, _ = get_object_pose("wooden tray")
    
    open_gripper()
    # Move 10 cm above before grasping
    goto_pose(can_pos, can_quat, z_approach=0.1)
    goto_pose(can_pos, can_quat)
    close_gripper()
    
    # Move 10 cm above to avoid collisions before going to target
    lift_pos = can_pos.copy()
    lift_pos[2] += 0.1
    goto_pose(lift_pos, can_quat)
    
    # Target height is object's z-coord + 5cm as instructed
    target_pos = tray_pos.copy()
    target_pos[2] = can_pos[2] + 0.05
    
    # Move to tray and place
    goto_pose(target_pos, can_quat, z_approach=0.1)
    goto_pose(target_pos, can_quat)
    open_gripper()
    
    # Move 10 cm above tray before returning home
    post_place_pos = target_pos.copy()
    post_place_pos[2] += 0.1
    goto_pose(post_place_pos, can_quat)
    
    home_pose()
else:
    print("can second from right black can is not empty.")
    breakpoint_code_block()

# Code block 3
import numpy as np

print("THOUGHT: The black can was not empty. I will now check the rightmost red can. | ACTION: Lift rightmost red can")
weight = get_weight("rightmost red can")
print(f"rightmost red can weight: {weight}")

if weight < 0.1:
    print("Empty can confirmed: rightmost red can")
    can_pos, can_quat = get_object_pose("rightmost red can")
    tray_pos, _ = get_object_pose("wooden tray")
    
    open_gripper()
    # Move 10 cm above before grasping
    goto_pose(can_pos, can_quat, z_approach=0.1)
    goto_pose(can_pos, can_quat)
    close_gripper()
    
    # Move 10 cm above to avoid collisions before going to target
    lift_pos = can_pos.copy()
    lift_pos[2] += 0.1
    goto_pose(lift_pos, can_quat)
    
    # Target height is object's z-coord + 5cm as instructed
    target_pos = tray_pos.copy()
    target_pos[2] = can_pos[2] + 0.05
    
    # Move to tray and place
    goto_pose(target_pos, can_quat, z_approach=0.1)
    goto_pose(target_pos, can_quat)
    open_gripper()
    
    # Move 10 cm above tray before returning home
    post_place_pos = target_pos.copy()
    post_place_pos[2] += 0.1
    goto_pose(post_place_pos, can_quat)
    
    home_pose()
else:
    print("can rightmost red can is not empty.")
    breakpoint_code_block()

# Code block 4
import numpy as np

print("THOUGHT: The empty can has been successfully identified and moved to the wooden tray. The task is now complete. | ACTION: Return to home pose")
home_pose()