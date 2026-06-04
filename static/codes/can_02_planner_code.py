# Code block 0
import numpy as np

cans = [
    "leftmost blue patterned can",
    "second from left green can with a yellow straw",
    "second from right black can with green claw marks",
    "rightmost red can with a yellow straw"
]

tray_name = "rectangular wooden tray"

for can in cans:
    print(f"THOUGHT: Need to check if the {can} is empty by measuring its weight. | ACTION: Lift {can}")
    weight = get_weight(can)
    print(f"Measured weight of {can}: {weight:.3f} kg")
    
    if weight < 0.1:
        print(f"Empty can confirmed: {can}.")
        
        # Get pick pose of the confirmed empty can
        can_pos, can_quat = get_object_pose(can)
        open_gripper()
        
        # Approach from 10cm above and move to grasp pose
        goto_pose(can_pos, can_quat, z_approach=0.1)
        close_gripper()
        
        # Move 10 cm above the object before going to target to avoid collisions
        goto_pose(can_pos + np.array([0.0, 0.0, 0.1]), can_quat)
        
        # Locate target destination (wooden tray)
        tray_pos, _ = get_object_pose(tray_name)
        
        # Calculate safe placement pose: Use tray X and Y, and maintain can's original Z plus an offset for tray thickness
        place_pos = np.array([tray_pos[0], tray_pos[1], can_pos[2] + 0.03])
        
        # Approach from 10cm above and place on the tray
        goto_pose(place_pos, can_quat, z_approach=0.1)
        open_gripper()
        
        # Move 10 cm above the tray and object before going to home pose to avoid collisions
        goto_pose(place_pos + np.array([0.0, 0.0, 0.1]), can_quat)
        home_pose()
        
        print("Task successfully completed. Empty can relocated to the wooden tray.")
        break
    else:
        print(f"can {can} is not empty. Placed back in its original coordinates.")
        print("Request next observation")