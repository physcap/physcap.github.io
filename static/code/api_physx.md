    ...
    def get_mass(self, object_name: str) -> float:
        """Measure an object's mass, in kilograms.

        Grasps the object, lifts it, infers mass from joint load, averages a
        few readings, and returns the object to where it found it. Gripper
        must be empty before calling.
        Make sure nothing is in the gripper before calling this.

        Args:
            object_name: The object to weigh. Molmo2 locates it from this name
                alone, so make it unambiguous — give colour and position
                (e.g. "the left-most red cube"), not just "cube".

        Returns:
            Mass in kilograms, +/-30 g noise. Slightly-negative readings on
            very light objects are noise, not failure. A large negative value
            means the grasp failed; nan means no reading was taken — reweigh
            in either case.

        Example:
            mass = get_mass("the left-most red cube")
            print(f"left-most red cube: {mass:.3f} kg")
        """
        try:
            mass = self._env.measure_object_mass(object_name)
            print(f"[get_mass] '{object_name}' has mass {mass:.4f} kg")
            save_property_to_knowledge(self._env, object_name, "mass", mass, "kg")
            return mass
        except Exception as exc:
            print(f"Warning: Failed to measure mass of '{object_name}': {exc}")
            return float("nan")

    def get_stiffness(self, object_name: str) -> int:
        """Measure the stiffness of an object by probing its surface.

        This function executes a controlled probing motion on the object,
        measures force and displacement, and classifies the stiffness level.

        Make sure nothing is in gripper before calling this function.

        Returns a stiffness level from 1 (soft) to 5 (rigid):
            1 = Ultra-Soft   (e.g., sponges, foams, soft plush)
            2 = Soft         (e.g., soft rubbers, ripe fruit, silicone)
            3 = Semi-Rigid   (e.g., cardboard, ripe fruit)
            4 = Stiff        (e.g., hardwood, dense polymers)
            5 = Rigid        (e.g., metal, ceramics, stone)
        Returns 0 if measurement fails. You may need to test is again.

        Args:
            object_name: Name of the object to measure (e.g., "red_cube", "apple")
            This function will use Molmo2 for object detecting, it will only take in the current object name as input.
            Make sure that the given object name is clear and will not cause any ambiguity.
            It is adviced that the positional description (left-most, second from right, etc.), color (and object's name if possible) is provided in the object name.

        Returns:
            stiffness_level: Integer 1-5 indicating stiffness. Returns 0 if measurement fails.

        Example:
            stiffness = get_stiffness("apple")
            if stiffness == 2:
                print("Apple stiffness is level 2:soft - likely ripe")
            elif stiffness == 3:
                print("Apple stiffness is level 3:firm - handle carefully")
            elif stiffness == 0:
                print("Apple stiffness is level 0:measurement failed")
        """
        try:
            stiffness = self._env.measure_object_stiffness(object_name)
            print(f"[get_stiffness] '{object_name}' stiffness level: {stiffness}/5")
            _save_property_to_knowledge(self._env, object_name, "stiffness", stiffness, "level")
            return stiffness
        except Exception as e:
            print(f"Warning: Failed to measure stiffness of '{object_name}': {e}")
            return 0
    ...
