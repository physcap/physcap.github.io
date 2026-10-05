# Code block 0
object_name = "green avocado on the far left. There are the fruits on the table are avocados, please point to the one that is the green avocado on the far left."
stiffness = get_stiffness(object_name)

print("THOUGHT: I need to test the avocados one by one to find the ripe one. I will start by measuring the stiffness of the green avocado on the far left. | ACTION: Gently squeeze avocado_green_far_left.")
print(f"Stiffness of avocado_green_far_left: {stiffness}")

if stiffness > 0:
    if stiffness <= 2:
        print("Ripe avocado confirmed: avocado_green_far_left.")
    else:
        print("Avocado avocado_green_far_left is unripe.")
else:
    print("Measurement failed for avocado_green_far_left.")

breakpoint_code_block()

# Code block 1
object_name = "avocado second from the left. There are the fruits on the table are avocados, please point to the one that is the avocado second from the left."
stiffness = get_stiffness(object_name)

print("THOUGHT: The green avocado on the far left was unripe. I am now checking the stiffness of the avocado second from the left. | ACTION: Gently squeeze avocado_middle_left.")
print(f"Stiffness of avocado_middle_left: {stiffness}")

if stiffness > 0:
    if stiffness <= 2:
        print("Ripe avocado confirmed: avocado_middle_left.")
        
        # Proceed to pick and place
        pos, quat = get_object_pose(object_name)
        open_gripper()
        goto_pose(pos, z_approach=0.1)
        goto_pose(pos)
        close_gripper()
        goto_pose(pos, z_approach=0.1)
        
        # Target destination
        tray_pos, tray_quat = get_object_pose("wooden tray")
        tray_pos[2] = pos[2] + 0.05
        
        goto_pose(tray_pos, z_approach=0.1)
        goto_pose(tray_pos)
        open_gripper()
        goto_pose(tray_pos, z_approach=0.1)
        
        home_pose()
    else:
        print("Avocado avocado_middle_left is unripe.")
else:
    print("Measurement failed for avocado_middle_left.")

breakpoint_code_block()

# Code block 2
object_name = "avocado second from the right. There are the fruits on the table are avocados, please point to the one that is the avocado second from the right."
stiffness = get_stiffness(object_name)

print("THOUGHT: The first two avocados were unripe. I will now check the stiffness of the avocado second from the right. | ACTION: Gently squeeze avocado_middle_right.")
print(f"Stiffness of avocado_middle_right: {stiffness}")

if stiffness > 0:
    if stiffness <= 2:
        print("Ripe avocado confirmed: avocado_middle_right.")
        
        # Proceed to pick and place
        pos, quat = get_object_pose(object_name)
        open_gripper()
        goto_pose(pos, z_approach=0.1)
        goto_pose(pos)
        close_gripper()
        goto_pose(pos, z_approach=0.1)
        
        # Target destination
        tray_pos, tray_quat = get_object_pose("wooden tray")
        tray_pos[2] = pos[2] + 0.05
        
        goto_pose(tray_pos, z_approach=0.1)
        goto_pose(tray_pos)
        open_gripper()
        goto_pose(tray_pos, z_approach=0.1)
        
        home_pose()
    else:
        print("Avocado avocado_middle_right is unripe.")
else:
    print("Measurement failed for avocado_middle_right.")

breakpoint_code_block()

# Code block 3
object_name = "avocado on the far right. There are the fruits on the table are avocados, please point to the one that is the avocado on the far right."
stiffness = get_stiffness(object_name)

print("THOUGHT: The first three avocados tested were unripe. I will now check the stiffness of the final avocado on the far right. | ACTION: Gently squeeze avocado_far_right.")
print(f"Stiffness of avocado_far_right: {stiffness}")

if stiffness > 0:
    if stiffness <= 2:
        print("Ripe avocado confirmed: avocado_far_right.")
        
        # Proceed to pick and place
        pos, quat = get_object_pose(object_name)
        open_gripper()
        goto_pose(pos, z_approach=0.1)
        goto_pose(pos)
        close_gripper()
        goto_pose(pos, z_approach=0.1)
        
        # Target destination
        tray_pos, tray_quat = get_object_pose("wooden tray")
        tray_pos[2] = pos[2] + 0.05
        
        goto_pose(tray_pos, z_approach=0.1)
        goto_pose(tray_pos)
        open_gripper()
        goto_pose(tray_pos, z_approach=0.1)
        
        home_pose()
    else:
        print("Avocado avocado_far_right is unripe.")
        print("All avocados have been physically tested and confirmed unripe.")
else:
    print("Measurement failed for avocado_far_right.")

breakpoint_code_block()

# Code block 4
print("THOUGHT: The ripe avocado (far right) has been successfully identified and relocated to the wooden tray. The arm has returned to the home position, and the task is fully complete. | ACTION: Terminate task.")
print("Task successfully completed.")