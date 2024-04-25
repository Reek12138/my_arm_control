import numpy as np
from math import pi, cos, sin
import modern_robotics as mr

def dh_transform(a, alpha, d, theta):
    """
    Calculate the transformation matrix using D-H parameters.
    """
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, a],
        [np.sin(theta) * np.cos(alpha), np.cos(theta) * np.cos(alpha), -np.sin(alpha), -np.sin(alpha) * d],
        [np.sin(theta) * np.sin(alpha), np.cos(theta) * np.sin(alpha), np.cos(alpha), np.cos(alpha) * d],
        [0, 0, 0, 1]
    ])

def forward_kinematics(joints):
    # input: joint angles [joint1, joint2, joint3]
    # output: the position of end effector [x, y, z]
    # add your code here to complete the computation

    link1z = 0.065
    link2z = 0.039
    link3x = 0.050
    link3z = 0.150
    link4x = 0.150
    joint1 = joints[0]
    joint2 = joints[1]
    joint3 = joints[2]

    a = [0, 0.050, 0.150]  # Example values
    alpha = [np.pi/2, 0, 0]  # Example values
    d = [0.065, 0, 0]  # Example values

    # Base transformation matrix (identity if at origin)
    T = np.eye(4)

    # Compute the transformation matrix for each joint and multiply
    for i in range(len(joints)):
        theta = joints[i]
        Ti = dh_transform(a[i], alpha[i], d[i], theta)
        T = np.dot(T, Ti)

    # Extract the position [x, y, z] from the transformation matrix
    x = T[0, 3]
    y = T[1, 3]
    z = T[2, 3]

    return [x, y, z]
