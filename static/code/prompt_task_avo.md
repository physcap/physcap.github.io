# Task: Find the ripe avocado

## Environment
- A table surface containing four avocados.
- One avocado is ripe; the others are unripe.
- A target destination designated by a wooden tray.

## Objective
Systematically interact with the avocados to identify the ripe one and relocate it to the wooden tray.

## Operational Protocol
1. Observe & Anchor: Analyze the image. Identify all avocados and assign unique IDs based on color and position (e.g., "avocado_dark_left", "avocado_green_center").
2. Reason: Output the reasoning for the proposed action.
   - Output Format: THOUGHT: [Reasoning] | ACTION: [Gently squeeze Avocado ID].
3. Evaluate:
   - An avocado is considered ripe if it is soft (stiffness level <= 2).
   - If NOT ripe: State "Avocado [ID] is unripe." Leave it in its original position. Request next observation.
   - If ripe: Announce "Ripe avocado confirmed: [ID]." Proceed to pick and place the avocado onto the wooden tray.

## Constraints
- Sequential Interaction: Interact with exactly one object per reasoning cycle.
- State Tracking: Maintain a strict list of "Checked" vs. "Unchecked" IDs to prevent redundant loops.
- Termination: End the task only when the ripe avocado is successfully placed onto the wooden tray, or all avocados have been physically tested and confirmed unripe.
