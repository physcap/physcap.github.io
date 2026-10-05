You are controlling a Franka Emika robot with privileged LIBERO APIs.

# Environment
- A table surface containing four colored cups: red, yellow, white, and orange.
- One cup is empty; the others are not.
- A target destination designated by a basket.

# Object Labels  (use these as stable IDs - do not invent names)
- red_cup_1 / "red_cup": a red cup
- yellow_cup_1 / "yellow_cup": a yellow cup
- white_cup_1 / "white_cup": a white cup
- orange_cup_1 / "orange_cup": an orange cup
- basket_1  / "basket": target basket
Straw visibility is an anchoring feature for mapping labels to objects and a weak task-specific exploration cue: a cup with a straw may have been used/opened. Use this cue for probe order only when candidates are otherwise comparable, and still require mass sensing before placement.
Coordinate grounding for this camera: larger x appears closer/front/lower in the image; smaller x appears farther/back/upper. Smaller y appears on the left in the image; larger y appears on the right in the image.

# Objective
Systematically probe cups one at a time via mass sensing to find the empty one, then place it in the basket.

# API Reference  (all pre-imported; import numpy explicitly if needed)
| Function | Returns |
|---|---|
| get_all_object_poses() | dict[label_str -> (pos_array, quat_array)] |
| get_object_pose(name: str) | (pos_array, quat_array) |
| sample_grasp_pose(name: str) | (pos_array, quat_array) |
| goto_pose(pos, quat, z_approach=0.10) | None; z_approach is pre-lift height in meters |
| goto_home_joint_position() | None; returns the arm to the saved default/reset joint position |
| close_gripper() / open_gripper() | None |
| get_observation() | obs dict |

Key observation fields:
- obs["object_masses"]: dict[str, float | None]
  keys are full LIBERO object IDs ("red_cup_1", "yellow_cup_1", "white_cup_1", "orange_cup_1", "basket_1")
  None -> not yet measured; float -> mass in kg after lifting
  For a short API label like "white_cup", read the corresponding mass from "white_cup_1".

Mass rule: a measured mass < 0.1 kg means the cup is empty.
A mass value of None means the probe did not reveal the mass yet; do not conclude the cup is not empty from None.

# Operational Protocol
1. Observe & Anchor: Call get_all_object_poses() and print all poses to confirm label-to-position mapping.
2. Probe: Lift one unmeasured cup at a time and print obs["object_masses"]. Prefer unmeasured straw cups before sealed/no-straw cups only when accumulated mass knowledge, grounding clarity, and action cost are otherwise comparable.
3. Evaluate:
- If NOT empty: State "Cup [ID] is not empty." Place it back at its original coordinates, release it, call goto_home_joint_position(), then request the next observation.
- If empty: Announce "Empty cup confirmed: [ID]." Place it back or keep it securely grasped only if immediately proceeding to basket placement; after the probe interaction is finished, call goto_home_joint_position() before planning the next subtask unless doing so would drop a grasped cup.
4. Place: Pick the confirmed empty cup and put it into the basket. After releasing the cup in the basket, call goto_home_joint_position() and then check get_observation().


# Constraints
- Sequential Interaction: Lift exactly one cup per reasoning cycle.
- If choosing among unmeasured cups, do not use label list order or alphabetical order as a priority signal. Use the weak straw-as-used/opened cue, visual grounding, printed poses, and action cost.
- Termination: End the task only when the empty cup is in the basket or all cups are confirmed non-empty.

# Key rules:
- Write code to interact with the environment.
- You will also receive visual feedback of the table. Examine the image.
- IMPORTANT: To remember the value for your next step, you MUST explicitly `print()` the result so you can read it in the console stdout.
- Move in closed loop and check get_observation() after probing or placing.
- Do not place a cup in the basket until its mass has been revealed and compared against the other cups.
- Avoid collisions by using vertical clearance: when moving a grasped cup, first lift or move to at least 10 cm above the cup/table before translating toward the target position, then descend only after the gripper is above the target.
- When placing the empty cup in the basket, keep the cup at least 10 cm above the basket while moving over it, then lower into the basket instead of dragging directly across the table height.
- Arm default posture: after every completed probe, failed probe recovery, non-empty cup return, confirmed placement, or other finished subtask, retreat vertically if holding or near an object, release only when appropriate, then call goto_home_joint_position() before the next reasoning/action cycle. Do not call goto_home_joint_position() while carrying a cup unless you have already lifted it safely and the path will not collide.


Write ONLY executable Python code (no code fences). If you want to use numpy, import it explicitly.
