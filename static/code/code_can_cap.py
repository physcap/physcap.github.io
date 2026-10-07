# Code block 0
import numpy as np

print("THOUGHT: To find the empty can, I will test the cans one by one starting from the left. First, I will lift the green Sprite can to see if it is the empty one. | ACTION: Lift green Sprite can")

open_gripper()
sprite_pos, sprite_quat = get_object_pose("green Sprite can")
goto_pose(sprite_pos, sprite_quat, z_approach=0.1)
close_gripper()

lift_pos = sprite_pos.copy()
lift_pos[2] += 0.1
goto_pose(lift_pos, sprite_quat)

breakpoint_code_block()

# Code block 1
import numpy as np

print("THOUGHT: The green Sprite can was successfully lifted without slipping. Since a full can would likely slip from the gripper due to its mass, this indicates the green can is empty. I will now place it on the wooden tray to complete the task. | ACTION: Place green Sprite can on the wooden tray")

tray_pos, tray_quat = get_object_pose("wooden tray")

# When placing object on for the wooden tray, aim for the object's z-coordinate + 5 cm above the tray's surface
place_pos = tray_pos.copy()
place_pos[2] += 0.05

# Move 10 cm above the target position before going to it to avoid collisions
hover_pos = place_pos.copy()
hover_pos[2] += 0.10
goto_pose(hover_pos, tray_quat)

# Lower to the placing position
goto_pose(place_pos, tray_quat)
open_gripper()

# Lift arm 20 cm above the tray and object before going to home pose
post_place_pos = place_pos.copy()
post_place_pos[2] += 0.20
goto_pose(post_place_pos, tray_quat)

# Return home
home_pose()

breakpoint_code_block()