import math

# Define the segment lengths of the robotic leg
L1 = 5.0   # Length of the coxa
L2 = 10.0  # Length of the femur
L3 = 15.0  # Length of the tibia
b = 0.0    # Optional vertical base offset (can be zero)

def inverse_kinematics(x_target, y_target, z_target):
   
    # Calculate the rotation angle at the coxa joint
    q1 = math.atan2(y_target, x_target)

    # Horizontal distance from the base to the target point
    horizontal_dist = math.hypot(x_target, y_target)

    # Vertical displacement from the femur base joint
    vertical_offset = z_target - L1 - b

    # Use cosine law to determine the tibia angle
    cos_gamma = (horizontal_dist**2 + vertical_offset**2 - L2**2 - L3**2) / (2 * L2 * L3)

    # Check if the point is physically reachable
    if cos_gamma < -1 or cos_gamma > 1:
        return None, None, None

    # Tibia joint angle
    q3 = math.acos(cos_gamma)

    # Intermediate values for femur angle calculation
    sin_gamma = math.sin(q3)
    cos_gamma_actual = math.cos(q3)

    q2 = math.atan2(vertical_offset, horizontal_dist) - math.atan2(sin_gamma * L3, L2 + cos_gamma_actual * L3)

    # Convert radians to degrees
    alpha = math.degrees(q1)
    beta = math.degrees(q2)
    gamma = math.degrees(q3)

    return alpha, beta, gamma


def test_inverse_kinematics():
    print("\n=== Running Inverse Kinematics Tests ===\n")

    scenarios = [
        {"desc": "Standard reachable point", "x": 10, "y": 5, "z": -10},
        {"desc": "Very close to origin", "x": 1, "y": 1, "z": -2},
        {"desc": "Max extension near limit", "x": 25, "y": 0, "z": -5},
        {"desc": "Beyond reachable range", "x": 35, "y": 10, "z": 0},
        {"desc": "Deep below platform", "x": 5, "y": 5, "z": -30},
    ]

    for idx, case in enumerate(scenarios, start=1):
        xt, yt, zt = case["x"], case["y"], case["z"]
        print(f"Test {idx}: {case['desc']}")
        print(f" Target Coordinates => x: {xt}, y: {yt}, z: {zt}")

        result = inverse_kinematics(xt, yt, zt)

        if result == (None, None, None):
            print("  ➤ Result: Unreachable position.\n")
        else:
            a, b, g = result
            print("  ➤ Result: Reachable.")
            print(f"     Coxa  (α): {a:.2f}°")
            print(f"     Femur (β): {b:.2f}°")
            print(f"     Tibia (γ): {g:.2f}°\n")



if __name__ == "__main__":
    try:
        x_in = float(input("Enter x-coordinate of the foot: "))
        y_in = float(input("Enter y-coordinate of the foot: "))
        z_in = float(input("Enter z-coordinate of the foot: "))

        ik_result = inverse_kinematics(x_in, y_in, z_in)

        if ik_result == (None, None, None):
            print("Target is unreachable.")
        else:
            a_deg, b_deg, g_deg = ik_result
            print("\nCalculated Joint Angles:")
            print(f"Coxa  (α): {a_deg:.2f}°")
            print(f"Femur (β): {b_deg:.2f}°")
            print(f"Tibia (γ): {g_deg:.2f}°")

        # Also run tests
        test_inverse_kinematics()

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
