# Code block 0
import numpy as np

print("THOUGHT: The current step is to test the dark avocado left of center (second from left). I will measure its stiffness to determine if it's ripe. If it is soft (stiffness <= 2), I will relocate it to the wooden tray. | ACTION: Gently squeeze avocado_dark_left")

avocado_name = "There are the fruits on the table are avocados, please point to the one that is the dark avocado second from the left."
stiffness = get_stiffness(avocado_name)
print(f"Stiffness of avocado_dark_left: {stiffness}")

if stiffness > 0 and stiffness <= 2:
    print("Ripe avocado confirmed: avocado_dark_left.")
    
    # Proceed to pick up the ripe avocado
    pos, quat = get_object_pose(avocado_name)
    open_gripper()
    goto_pose(pos, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object before going to the target position to avoid collisions
    goto_pose(pos + np.array([0.0, 0.0, 0.1]))
    
    # Get tray location
    tray_pos, tray_quat = get_object_pose("wooden tray")
    
    # Aim for the object's z-coordinate + 5 cm above the tray's surface
    target_pos = np.array([tray_pos[0], tray_pos[1], pos[2] + 0.05])
    goto_pose(target_pos, z_approach=0.1)
    open_gripper()
    
    # Move 10 cm above the tray and object before going to home pose
    goto_pose(target_pos + np.array([0.0, 0.0, 0.1]))
    home_pose()
else:
    print("Avocado avocado_dark_left is unripe.")
    # Request next observation
    breakpoint_code_block()

# Code block 1
import numpy as np

print("THOUGHT: The previous avocado was semi-rigid (unripe). The current step is to test the right-most dark avocado. I will measure its stiffness to determine if it is ripe. If soft (<= 2), I will relocate it to the wooden tray. | ACTION: Gently squeeze right-most dark avocado")

avocado_name = "There are the fruits on the table are avocados, please point to the one that is the right-most dark avocado."
stiffness = get_stiffness(avocado_name)
print(f"Stiffness of right-most dark avocado: {stiffness}")

if stiffness > 0 and stiffness <= 2:
    print("Ripe avocado confirmed: avocado_dark_right.")
    
    # Proceed to pick up the ripe avocado
    pos, quat = get_object_pose(avocado_name)
    open_gripper()
    goto_pose(pos, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object before going to the target position to avoid collisions
    goto_pose(pos + np.array([0.0, 0.0, 0.1]))
    
    # Get tray location
    tray_pos, tray_quat = get_object_pose("wooden tray")
    
    # Aim for the object's z-coordinate + 5 cm above the tray's surface
    target_pos = np.array([tray_pos[0], tray_pos[1], pos[2] + 0.05])
    goto_pose(target_pos, z_approach=0.1)
    open_gripper()
    
    # Move 10 cm above the tray and object before going to home pose
    goto_pose(target_pos + np.array([0.0, 0.0, 0.1]))
    home_pose()
else:
    print("Avocado avocado_dark_right is unripe.")
    # Request next observation
    breakpoint_code_block()

# Code block 2
print("THOUGHT: The right-most dark avocado was successfully identified as the ripe avocado (stiffness level 2) and has already been relocated to the wooden tray. The operational protocol has been fulfilled. | ACTION: Conclude task.")