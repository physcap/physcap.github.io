# Code block 0
import numpy as np

cans = [
    "black Monster Energy can on the far left",
    "green Sprite can with an orange straw",
    "blue Monster Energy can",
    "red Coca-Cola can with a yellow straw on the far right"
]

for can in cans:
    print(f"THOUGHT: I need to check if the {can} is empty by measuring its mass. | ACTION: Lift {can}.")
    
    # Measure the mass of the can
    mass = get_mass(can)
    
    # Retry if the measurement failed
    while np.isnan(mass) or mass < -0.1:
        print(f"Mass measurement failed for {can}. Retrying...")
        mass = get_mass(can)
        
    print(f"Mass of {can}: {mass:.3f} kg")
    
    if mass < 0.1:
        print(f"Empty can confirmed: {can}.")
        can_pos, can_quat = get_object_pose(can)
        tray_pos, tray_quat = get_object_pose("wooden tray")
        
        open_gripper()
        
        # Approach and grasp the empty can
        goto_pose(can_pos, can_quat, z_approach=0.1)
        close_gripper()
        
        # Move 10 cm above the object before going to the target position
        goto_pose(can_pos + np.array([0.0, 0.0, 0.1]), can_quat)
        
        # Aim for the object's z-coordinate + 5 cm above the tray's surface
        target_pos = np.array([tray_pos[0], tray_pos[1], can_pos[2] + 0.05])
        
        # Move to wooden tray
        goto_pose(target_pos, can_quat, z_approach=0.1)
        open_gripper()
        
        # Lift arm 20 cm above the tray and object before going to home pose
        goto_pose(target_pos + np.array([0.0, 0.0, 0.2]), can_quat)
        home_pose()
        break
    else:
        print(f"can {can} is not empty.")