# Key rules:
- Write code to interact with the environment.
- You will also receive visual feedback of the table. Examine the image.
- IMPORTANT: To remember the value for your next step, you MUST explicitly `print()` the result so you can read it in the console stdout.

- Call get_object_pose(object_name) to find objects.
- When moving objects, move 10 cm above the object before going to the target position to avoid collisions.
- When placing an object on the wooden tray, aim for the object's z-coordinate + 5 cm above the tray's surface so that the gripper's height matches the object's height.
- After placing objects on the wooden tray, lift the arm 20 cm above the tray and object before going to home pose to avoid collisions.
- Go to home position after you've successfully completed the task.

Write ONLY executable Python code (no code fences).
