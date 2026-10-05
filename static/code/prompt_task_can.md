# Task: Find the empty can

## Environment
- A table surface containing four soft drink cans.
- One can is empty; the others are not.
- A target destination designated by a wooden tray.

## Objective
Systematically interact with the cans to identify the empty one and relocate it to the wooden tray.

## Operational Protocol
1. Observe & Anchor: Analyze the image. Identify all cans and assign IDs based on color and position (e.g., "Blue can left").
2. Reason: Output the reasoning for the proposed action.
   - Output Format: THOUGHT: [Reasoning] | ACTION: [Lift can ID].
3. Evaluate:
   - A can is classified as empty if the mass is below 0.1 kg.
   - If NOT empty: State "Can [ID] is not empty." Place it back at its original coordinates. Request next observation.
   - If empty: Announce "Empty can confirmed: [ID]." Proceed to pick and place the can onto the wooden tray.

## Constraints
- Sequential Interaction: Interact with exactly one object per reasoning cycle.
- State Tracking: Maintain a list of "Checked" vs. "Unchecked" IDs to prevent redundant loops.
- Termination: End the task only when the empty can is on the wooden tray or all cans are confirmed non-empty.
