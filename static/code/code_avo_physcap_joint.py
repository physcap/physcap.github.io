# Code block 0
print("THOUGHT: Measure the stiffness of the dark inner-left avocado to determine if it is ripe (stiffness <= 2). | ACTION: Gently squeeze avocado_inner_left_dark.")
stiffness = get_stiffness("There are the fruits on the table are avocados, please point to the one that is second from left dark avocado.")
print(f"Stiffness result for avocado_inner_left_dark: {stiffness}")

if 0 < stiffness <= 2:
    print("Ripe avocado confirmed: avocado_inner_left_dark.")
elif stiffness > 2:
    print("Avocado avocado_inner_left_dark is unripe.")
else:
    print("Measurement failed for avocado_inner_left_dark.")

breakpoint_code_block()

# Code block 1
print("THOUGHT: Measure the stiffness of the far right dark avocado to determine if it is ripe (stiffness <= 2). | ACTION: Gently squeeze avocado_dark_far_right.")
stiffness = get_stiffness("There are the fruits on the table are avocados, please point to the one that is far right dark avocado.")
print(f"Stiffness result for avocado_dark_far_right: {stiffness}")

if 0 < stiffness <= 2:
    print("Ripe avocado confirmed: avocado_dark_far_right.")
    open_gripper()
    pos, quat = get_object_pose("There are the fruits on the table are avocados, please point to the one that is far right dark avocado.")
    goto_pose(pos, quat, z_approach=0.1)
    goto_pose(pos, quat)
    close_gripper()
    goto_pose(pos, quat, z_approach=0.1)
    
    tray_pos, tray_quat = get_object_pose("wooden tray")
    place_pos = tray_pos.copy()
    place_pos[2] = tray_pos[2] + 0.05
    goto_pose(place_pos, tray_quat, z_approach=0.1)
    goto_pose(place_pos, tray_quat)
    open_gripper()
    goto_pose(place_pos, tray_quat, z_approach=0.1)
    
    home_pose()
elif stiffness > 2:
    print("Avocado avocado_dark_far_right is unripe.")
else:
    print("Measurement failed for avocado_dark_far_right.")

breakpoint_code_block()