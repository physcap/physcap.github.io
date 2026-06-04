# Code block 0
import numpy as np

print("THOUGHT: The four avocados on the table are visually identical with dark skin, making visual identification of the ripe one challenging. I must test them sequentially by physical interaction to find the ripe one. I will start from the left side and pick up the far-left avocado to evaluate it. | ACTION: Pick up the far-left avocado")

avo_prompt = "There are the fruits on the table are avocados, please point to the one that is the far-left avocado."
avo_pos, avo_quat = get_object_pose(avo_prompt)

open_gripper()
# Move 10 cm above the object before going to the grasp position
goto_pose(avo_pos, avo_quat, z_approach=0.1)
goto_pose(avo_pos, avo_quat)
close_gripper()

# Lift the avocado 10 cm above to evaluate its ripeness
lift_pos = avo_pos.copy()
lift_pos[2] += 0.1
goto_pose(lift_pos, avo_quat)

print("Currently holding the far-left avocado. Request next observation to evaluate if it is ripe.")
breakpoint_code_block()

# Code block 1
print("THOUGHT: The current avocado does not feel soft and yields no indication of being ripe. I will mark it as unripe, return it to its original position, and request the next observation to proceed with the next avocado. | ACTION: Place the far-left avocado back to its original position.")

# Place the far-left avocado back to its original position
goto_pose(avo_pos, avo_quat)
open_gripper()

# Move up to avoid collision
goto_pose(lift_pos, avo_quat)

# Go to home position
home_pose()

print("Avocado far-left is unripe.")
breakpoint_code_block()

# Code block 2
import numpy as np

print("THOUGHT: The far-left avocado was unripe. I must evaluate the next avocado. I will move to the middle-left avocado, pick it up, and check its ripeness. | ACTION: Pick up the middle-left avocado.")

avo_prompt = "There are the fruits on the table are avocados, please point to the one that is the middle-left avocado."
avo_pos, avo_quat = get_object_pose(avo_prompt)

open_gripper()
# Move 10 cm above the object before going to the grasp position
goto_pose(avo_pos, avo_quat, z_approach=0.1)
goto_pose(avo_pos, avo_quat)
close_gripper()

# Lift the avocado 10 cm above to evaluate its ripeness
lift_pos = avo_pos.copy()
lift_pos[2] += 0.1
goto_pose(lift_pos, avo_quat)

print("Currently holding the middle-left avocado. Request next observation to evaluate if it is ripe.")
breakpoint_code_block()

# Code block 3
import numpy as np

print("THOUGHT: The current avocado feels soft and yields to gentle pressure, indicating it is ripe. I will place it in the wooden tray. | ACTION: Place the middle-left avocado into the wooden tray.")
print("Ripe avocado confirmed: middle-left avocado.")

tray_prompt = "the wooden tray"
tray_pos, _ = get_object_pose(tray_prompt)

# Aim for the tray's z-coordinate + 5 cm above the tray's surface
place_pos = tray_pos.copy()
place_pos[2] += 0.05

# Move 10 cm above the tray before going to the target position
goto_pose(place_pos, avo_quat, z_approach=0.1)
goto_pose(place_pos, avo_quat)

open_gripper()

# After placing, move 10 cm above the tray and object
lift_pos = place_pos.copy()
lift_pos[2] += 0.1
goto_pose(lift_pos, avo_quat)

home_pose()