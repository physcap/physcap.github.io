# Code block 0
import numpy as np
import math

print("THOUGHT: I need to measure the mass of the green can to determine if it is the empty one. | ACTION: Lift can_1")

mass = get_mass("the green can second from the left")
print(f"Mass of can_1: {mass} kg")

if math.isnan(mass) or mass < -0.2:
    print("Measurement failed or grasp missed. Needs to be retried.")
elif mass < 0.1:
    print("EMPTY CAN: green can")
    can_pos, _ = get_object_pose("the green can second from the left")
    tray_pos, _ = get_object_pose("the wooden tray in the middle right")
    
    open_gripper()
    goto_pose(can_pos, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object to avoid collisions
    goto_pose(can_pos + np.array([0.0, 0.0, 0.1]))
    
    # Place object on the wooden tray (aim for object's z-coordinate + 5 cm above tray)
    place_pos = np.array([tray_pos[0], tray_pos[1], can_pos[2] + 0.05])
    goto_pose(place_pos, z_approach=0.1)
    open_gripper()
    
    # Lift arm 20 cm above the tray and object before going home
    goto_pose(place_pos + np.array([0.0, 0.0, 0.2]))
    home_pose()
else:
    print("can can_1 is not empty.")
    # The can is already placed back by get_mass(), just go back to home pose.
    home_pose()

breakpoint_code_block()

# Code block 1
import numpy as np
import math

print("THOUGHT: I need to measure the mass of the red can to determine if it is the empty one. | ACTION: Lift can_2")

mass = get_mass("the red can second from the right")
print(f"Mass of can_2: {mass} kg")

if math.isnan(mass) or mass < -0.2:
    print("Measurement failed or grasp missed. Needs to be retried.")
elif mass < 0.1:
    print("EMPTY CAN: red can")
    can_pos, _ = get_object_pose("the red can second from the right")
    tray_pos, _ = get_object_pose("the wooden tray in the middle right")
    
    open_gripper()
    goto_pose(can_pos, z_approach=0.1)
    close_gripper()
    
    # Move 10 cm above the object to avoid collisions
    goto_pose(can_pos + np.array([0.0, 0.0, 0.1]))
    
    # Place object on the wooden tray (aim for object's z-coordinate + 5 cm above tray)
    place_pos = np.array([tray_pos[0], tray_pos[1], can_pos[2] + 0.05])
    goto_pose(place_pos, z_approach=0.1)
    open_gripper()
    
    # Lift arm 20 cm above the tray and object before going home
    goto_pose(place_pos + np.array([0.0, 0.0, 0.2]))
    home_pose()
else:
    print("can can_2 is not empty.")
    # The can is already placed back by get_mass(), just go back to home pose.
    home_pose()

breakpoint_code_block()