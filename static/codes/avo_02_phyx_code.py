# Code block 0
import numpy as np

avocado_id = "left-most green avocado"
full_object_name = "left-most green avocado. There are the fruits on the table are avocados, please point to the one that is left-most green avocado."

print("THOUGHT: I will systematically test each avocado starting from left to right. I will check the left-most green avocado first to see if it is ripe (stiffness <= 2). | ACTION: Gently squeeze left-most green avocado")

stiffness = get_stiffness(full_object_name)

if 1 <= stiffness <= 2:
    print(f"Ripe avocado confirmed: {avocado_id}.")
    
    open_gripper()
    
    # Get avocado position and approach to pick
    pos, quat = get_object_pose(full_object_name)
    goto_pose(pos, quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object
    high_pos = pos.copy()
    high_pos[2] += 0.1
    goto_pose(high_pos, quat)
    
    # Get wooden tray pose
    tray_pos, tray_quat = get_object_pose("wooden tray")
    
    # Calculate placement position (object's z-coord + 5cm)
    place_pos = tray_pos.copy()
    place_pos[2] = pos[2] + 0.05
    
    # Calculate fly-over position (10cm above placement position)
    place_high = place_pos.copy()
    place_high[2] += 0.1
    
    # Navigate to tray and place
    goto_pose(place_high, tray_quat)
    goto_pose(place_pos, tray_quat)
    open_gripper()
    
    # Move 10 cm above the tray before going home
    goto_pose(place_high, tray_quat)
    home_pose()

else:
    print(f"Avocado {avocado_id} is unripe.")

breakpoint_code_block()

# Code block 1
import numpy as np

avocado_id = "second from left dark avocado"
full_object_name = f"{avocado_id}. There are the fruits on the table are avocados, please point to the one that is {avocado_id}."

print(f"THOUGHT: I will systematically test each avocado. The first one was unripe, so I will check the {avocado_id} next to see if it is ripe (stiffness <= 2). | ACTION: Gently squeeze {avocado_id}")

stiffness = get_stiffness(full_object_name)

if 1 <= stiffness <= 2:
    print(f"Ripe avocado confirmed: {avocado_id}.")
    
    open_gripper()
    
    # Get avocado position and approach to pick
    pos, quat = get_object_pose(full_object_name)
    goto_pose(pos, quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object
    high_pos = pos.copy()
    high_pos[2] += 0.1
    goto_pose(high_pos, quat)
    
    # Get wooden tray pose
    tray_pos, tray_quat = get_object_pose("wooden tray. There is a wooden tray on the table, please point to it.")
    
    # Calculate placement position (object's z-coord + 5cm)
    place_pos = tray_pos.copy()
    place_pos[2] = pos[2] + 0.05
    
    # Calculate fly-over position (10cm above placement position)
    place_high = place_pos.copy()
    place_high[2] += 0.1
    
    # Navigate to tray and place
    goto_pose(place_high, tray_quat)
    goto_pose(place_pos, tray_quat)
    open_gripper()
    
    # Move 10 cm above the tray before going home
    goto_pose(place_high, tray_quat)
    home_pose()

else:
    print(f"Avocado {avocado_id} is unripe.")

breakpoint_code_block()

# Code block 2
import numpy as np

avocado_id = "third from left dark avocado"
full_object_name = f"{avocado_id}. There are the fruits on the table are avocados, please point to the one that is {avocado_id}."

print(f"THOUGHT: The first two avocados were unripe. I will check the {avocado_id} next to see if it is ripe (stiffness <= 2). | ACTION: Gently squeeze {avocado_id}")

stiffness = get_stiffness(full_object_name)

if 1 <= stiffness <= 2:
    print(f"Ripe avocado confirmed: {avocado_id}.")
    
    open_gripper()
    
    # Get avocado position and approach to pick
    pos, quat = get_object_pose(full_object_name)
    goto_pose(pos, quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object
    high_pos = pos.copy()
    high_pos[2] += 0.1
    goto_pose(high_pos, quat)
    
    # Get wooden tray pose
    tray_pos, tray_quat = get_object_pose("wooden tray. There is a wooden tray on the table, please point to it.")
    
    # Calculate placement position (object's z-coord + 5cm)
    place_pos = tray_pos.copy()
    place_pos[2] = pos[2] + 0.05
    
    # Calculate fly-over position (10cm above placement position)
    place_high = place_pos.copy()
    place_high[2] += 0.1
    
    # Navigate to tray and place
    goto_pose(place_high, tray_quat)
    goto_pose(place_pos, tray_quat)
    open_gripper()
    
    # Move 10 cm above the tray before going home
    goto_pose(place_high, tray_quat)
    home_pose()

else:
    print(f"Avocado {avocado_id} is unripe.")

breakpoint_code_block()

# Code block 3
import numpy as np

avocado_id = "right-most avocado"
full_object_name = f"{avocado_id}. There are the fruits on the table are avocados, please point to the one that is {avocado_id}."

print(f"THOUGHT: The first three avocados were unripe. I will check the {avocado_id} next to see if it is ripe (stiffness <= 2). | ACTION: Gently squeeze {avocado_id}")

stiffness = get_stiffness(full_object_name)

if 1 <= stiffness <= 2:
    print(f"Ripe avocado confirmed: {avocado_id}.")
    
    open_gripper()
    
    # Get avocado position and approach to pick
    pos, quat = get_object_pose(full_object_name)
    goto_pose(pos, quat, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object
    high_pos = pos.copy()
    high_pos[2] += 0.1
    goto_pose(high_pos, quat)
    
    # Get wooden tray pose
    tray_pos, tray_quat = get_object_pose("wooden tray. There is a wooden tray on the table, please point to it.")
    
    # Calculate placement position (object's z-coord + 5cm)
    place_pos = tray_pos.copy()
    place_pos[2] = pos[2] + 0.05
    
    # Calculate fly-over position (10cm above placement position)
    place_high = place_pos.copy()
    place_high[2] += 0.1
    
    # Navigate to tray and place
    goto_pose(place_high, tray_quat)
    goto_pose(place_pos, tray_quat)
    open_gripper()
    
    # Move 10 cm above the tray before going home
    goto_pose(place_high, tray_quat)
    home_pose()

else:
    print(f"Avocado {avocado_id} is unripe.")

breakpoint_code_block()