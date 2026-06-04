# Code block 0
import numpy as np

print("THOUGHT: By lifting the left brown cup and placing it on the wooden tray, I can check if one of the missing blue cubes is hidden underneath. | ACTION: Lift left brown cup")

open_gripper()

cup_pos, cup_quat = get_object_pose("left brown cup")
goto_pose(cup_pos, cup_quat, z_approach=0.10)
close_gripper()

# Move 10 cm above the object to avoid collisions
above_cup_pos = cup_pos.copy()
above_cup_pos[2] += 0.10
goto_pose(above_cup_pos, cup_quat)

tray_pos, tray_quat = get_object_pose("wooden tray")

# Aim for the object's z-coordinate + 5 cm above the tray's surface
place_pos = tray_pos.copy()
place_pos[2] = cup_pos[2] + 0.05

# Move to tray and descend
goto_pose(place_pos, cup_quat, z_approach=0.10)
open_gripper()

# Move 10 cm above the tray and object before going to home pose
above_place_pos = place_pos.copy()
above_place_pos[2] += 0.10
goto_pose(above_place_pos, cup_quat)

home_pose()
breakpoint_code_block()

# Code block 1
import numpy as np

print("THOUGHT: By lifting the center white cup and placing it on the wooden tray, I can check if another blue cube is hidden underneath. | ACTION: Lift center white cup")

open_gripper()
cup_pos, cup_quat = get_object_pose("center white cup")
goto_pose(cup_pos, cup_quat, z_approach=0.10)
close_gripper()

# Move 10 cm above to avoid collisions
above_cup_pos = cup_pos.copy()
above_cup_pos[2] += 0.10
goto_pose(above_cup_pos, cup_quat)

# Place on wooden tray
tray_pos, tray_quat = get_object_pose("wooden tray")
place_pos = tray_pos.copy()
# aimed at cup's z-coordinate + 5 cm above the tray's surface
place_pos[2] = cup_pos[2] + 0.05

goto_pose(place_pos, cup_quat, z_approach=0.10)
open_gripper()

# Move 10 cm above before going home
above_place_pos = place_pos.copy()
above_place_pos[2] += 0.10
goto_pose(above_place_pos, cup_quat)

home_pose()
breakpoint_code_block()

# Code block 2
import numpy as np

print("THOUGHT: By lifting the right brown cup and placing it on the wooden tray, I can check if the missing third blue cube is hidden underneath. | ACTION: Lift right brown cup")

open_gripper()
cup_pos, cup_quat = get_object_pose("right brown cup")
goto_pose(cup_pos, cup_quat, z_approach=0.10)
close_gripper()

# Move 10 cm above to avoid collisions
above_cup_pos = cup_pos.copy()
above_cup_pos[2] += 0.10
goto_pose(above_cup_pos, cup_quat)

# Place on wooden tray
tray_pos, tray_quat = get_object_pose("wooden tray")
place_pos = tray_pos.copy()
# aimed at cup's z-coordinate + 5 cm above the tray's surface
place_pos[2] = cup_pos[2] + 0.05

goto_pose(place_pos, cup_quat, z_approach=0.10)
open_gripper()

# Move 10 cm above before going home
above_place_pos = place_pos.copy()
above_place_pos[2] += 0.10
goto_pose(above_place_pos, cup_quat)

home_pose()
breakpoint_code_block()

# Code block 3
import numpy as np

print("THOUGHT: By lifting the tall brown cup and placing it on the wooden tray, I can check if the missing third blue cube is hidden underneath. | ACTION: Lift tall brown cup")

open_gripper()
cup_pos, cup_quat = get_object_pose("tall brown cup")
goto_pose(cup_pos, cup_quat, z_approach=0.10)
close_gripper()

# Move 10 cm above to avoid collisions
above_cup_pos = cup_pos.copy()
above_cup_pos[2] += 0.10
goto_pose(above_cup_pos, cup_quat)

# Place on wooden tray
tray_pos, tray_quat = get_object_pose("wooden tray")
place_pos = tray_pos.copy()
# aimed at cup's z-coordinate + 5 cm above the tray's surface
place_pos[2] = cup_pos[2] + 0.05

goto_pose(place_pos, cup_quat, z_approach=0.10)
open_gripper()

# Move 10 cm above before going home
above_place_pos = place_pos.copy()
above_place_pos[2] += 0.10
goto_pose(above_place_pos, cup_quat)

home_pose()
breakpoint_code_block()

# Code block 4
print("THOUGHT: The third blue cube was revealed underneath the tall brown cup. All three blue cubes are now in sight, and the task is successfully completed. | ACTION: None")