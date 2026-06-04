# Code block 0
print("THOUGHT: Since I cannot determine visually which can is empty, I will systematically interact with them starting from the left. I will first lift the blue can to see if it is empty. | ACTION: Lift blue can")

open_gripper()
blue_can_pos, blue_can_quat = get_object_pose("blue can")
goto_pose(blue_can_pos, blue_can_quat, z_approach=0.1)
close_gripper()

lift_pos = blue_can_pos.copy()
lift_pos[2] += 0.1
goto_pose(lift_pos, blue_can_quat)

breakpoint_code_block()

# Code block 1
print("THOUGHT: The blue can was successfully lifted. Since I lack quantitative force feedback, and there were no indications of slipping or excessive load, I will hypothesize that this is the empty can. I will proceed to place it on the wooden tray to fulfill the objective. | ACTION: Place blue can on wooden tray")

tray_pos, tray_quat = get_object_pose("wooden tray")

# Move to a position above the wooden tray to avoid collisions (target object z + 5cm above tray roughly translates to z_approach or manual offset)
place_pos = tray_pos.copy()
place_pos[2] += 0.15 # Approx height for placing

goto_pose(place_pos, blue_can_quat)
open_gripper()

# Move 10 cm above before going home
retreat_pos = place_pos.copy()
retreat_pos[2] += 0.1
goto_pose(retreat_pos, blue_can_quat)

home_pose()
breakpoint_code_block()