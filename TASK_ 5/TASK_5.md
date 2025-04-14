TASK 5 – Inverse Kinematics for Hexapod Robot Leg

#Task
This task implements the inverse kinematics for a single leg of a hexapod robot with three degrees of freedom (3-DOF). The goal is to compute the required joint angles so that the foot of the leg reaches a given point (x, y, z) in 3D space.

# Leg Structure
The robotic leg has 3 segments:

L1: Coxa (horizontal rotation)
L2: Femur (vertical lifting)
L3: Tibia (extension)
b: Optional base height from the ground (set to 0 for flat terrain)
#Working:
The function inverse_kinematics(x, y, z) computes:

Coxa angle (α) – Horizontal rotation using atan2(y, x)
Tibia angle (γ) – Using the law of cosines
Femur angle (β) – Using geometry and triangle analysis
Angles are returned in degrees
If the target point is unreachable (due to excessive distance or extreme angles), the function returns (None, None, None).

# Testing the Function
The test_inverse_kinematics() function runs five test cases:

Reachable and near origin
Far and extreme points
Unreachable cases
These help validate the correctness and physical limits of the system.
# User Input
At runtime, the user is prompted to enter custom coordinates. The code calculates and prints:

α: Coxa angle
β: Femur angle
γ: Tibia angle
 # Error Handling
The code includes try-except blocks to handle invalid numeric input from the user, improving reliability during testing and deployment.
