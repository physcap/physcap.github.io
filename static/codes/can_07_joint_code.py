# Code block 0
import numpy as np

can_id = "green can center-left"
print(f"THOUGHT: I will measure the weight of the {can_id} to check if it's the empty one. | ACTION: Lift can {can_id}")

weight = get_weight(can_id)
print(f"Weight of {can_id}: {weight:.3f} kg")

if weight < 0.1:
    print(f"Empty can confirmed: {can_id}.")
    
    pos, quat = get_object_pose(can_id)
    open_gripper()
    goto_pose(pos, quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object before going to the target position
    pos_above = pos.copy()
    pos_above[2] += 0.1
    goto_pose(pos_above, quat)
    
    # Move to the wooden tray and place it
    tray_pos, tray_quat = get_object_pose("small wooden tray")
    goto_pose(tray_pos, tray_quat, z_approach=0.1)
    open_gripper()
    
    # Move 10 cm above the tray and object before going to home pose
    tray_above = tray_pos.copy()
    tray_above[2] += 0.1
    goto_pose(tray_above, tray_quat)
    
    home_pose()
else:
    print(f"can {can_id} is not empty.")
    breakpoint_code_block()

# Code block 1
import numpy as np

can_id = "red can right"
print(f"THOUGHT: I will measure the weight of the {can_id} to check if it's the empty one. | ACTION: Lift can {can_id}")

weight = get_weight(can_id)
print(f"Weight of {can_id}: {weight:.3f} kg")

if weight < 0.1:
    print(f"Empty can confirmed: {can_id}.")
    
    pos, quat = get_object_pose(can_id)
    open_gripper()
    goto_pose(pos, quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object before going to the target position
    pos_above = pos.copy()
    pos_above[2] += 0.1
    goto_pose(pos_above, quat)
    
    # Move to the wooden tray and place it
    tray_pos, tray_quat = get_object_pose("small wooden tray")
    goto_pose(tray_pos, tray_quat, z_approach=0.1)
    open_gripper()
    
    # Move 10 cm above the tray and object before going to home pose
    tray_above = tray_pos.copy()
    tray_above[2] += 0.1
    goto_pose(tray_above, tray_quat)
    
    home_pose()
else:
    print(f"can {can_id} is not empty.")
    breakpoint_code_block()

# Code block 2
import numpy as np

can_id = "red can right"
print(f"THOUGHT: Based on accumulated knowledge, the {can_id} is the empty one. I will verify its weight and then relocate it to the small wooden tray. | ACTION: Lift can {can_id}")

weight = get_weight(can_id)
print(f"Weight of {can_id}: {weight:.3f} kg")

if weight < 0.1:
    print(f"Empty can confirmed: {can_id}.")
    
    # Get pose and pick up the empty can
    pos, quat = get_object_pose(can_id)
    open_gripper()
    goto_pose(pos, quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object before going to the target position
    pos_above = pos.copy()
    pos_above[2] += 0.1
    goto_pose(pos_above, quat)
    
    # Find the target wooden tray
    tray_pos, tray_quat = get_object_pose("small wooden tray")
    
    # Move to the wooden tray and place it
    goto_pose(tray_pos, tray_quat, z_approach=0.1)
    open_gripper()
    
    # Move 10 cm above the tray and object before going to home pose
    tray_above = tray_pos.copy()
    tray_above[2] += 0.1
    goto_pose(tray_above, tray_quat)
    
    # Return arm to rest pose after successfully completing the task
    home_pose()
else:
    print(f"can {can_id} is not empty.")