    ...
    def get_object_pose(self, object_name: str) -> tuple[np.ndarray, np.ndarray]:
        """Sample a grasp pose for an object.
        This function will use Molmo2 for object detection; it will only take in the current object name as input.
        Make sure that the given object name is clear and will not cause any ambiguity.
        It is advised that positional descriptions (left-most, second from right, etc.), color, and the object's name (if possible) are provided in the object name.
        Returns:
            position: (3,) XYZ in meters.
            quaternion_wxyz: (4,) WXYZ unit quaternion (often unused for 3DOF setups).
        """
        pos, _ = self._env._get_object_pose(object_name)
        return pos, np.array([1, 0, 0, 0])

    def goto_pose(
        self, position: np.ndarray, quaternion_wxyz: np.ndarray = None, z_approach: float = 0.0
    ) -> None:
        """Go to pose using Cartesian IK provided natively by the AgileX firmware.
        There is no need to call a second goto_pose with the same position and quaternion_wxyz after calling it with z_approach.
        Example:
        goto_pose(np.array([0.1, 0.2, 0.3])) # This controls the arm directly to position [0.1, 0.2, 0.3]
        goto_pose(np.array([0.1, 0.2, 0.3]), z_approach=0.05) # This controls the arm to position [0.1, 0.2, 0.3] + [0, 0, 0.05] and then moves to position [0.1, 0.2, 0.3]
        Args:
            position: (3,) XYZ in meters.
            quaternion_wxyz: (4,) WXYZ unit quaternion. Ignored in 3 DOF positioning.
            z_approach: (float) Z-axis distance offset for the goto_pose insertion approach motion. Will first arrive at position + z_approach meters in the Z-axis before moving to the requested pose. Useful for more precise grasp approaches. Default is 0.0.
        """
        pos = np.asarray(position, dtype=np.float64).reshape(3)
        
        if z_approach != 0.0:
            approach_pos = pos + np.array([0, 0, z_approach])
            self._env.move_to_cartesian_blocking(approach_pos)
            
        self._env.move_to_cartesian_blocking(pos)

    def open_gripper(self) -> None:
        """Open gripper fully."""
        self._env.open_gripper()

    def close_gripper(self) -> None:
        """Close gripper fully."""
        self._env.close_gripper()

    def home_pose(self) -> None:
        """Return the arm to its rest pose."""
        self._env.home_pose()

    def breakpoint_code_block(self) -> None:
        """Call this function to mark a significant checkpoint."""
        return None
    ...
