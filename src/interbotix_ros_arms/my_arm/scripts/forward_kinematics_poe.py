# -*- coding: utf-8 -*-

import numpy as np
from math import pi, cos, sin
import modern_robotics as mr

# def forward_kinematics(joints):
#     # input: joint angles [joint1, joint2, joint3]
#     # output: the position of end effector [x, y, z]
#     # add your code here to complete the computation

#     link1z = 0.065
#     link2z = 0.039
#     link3x = 0.050
#     link3z = 0.150
#     link4x = 0.150
#     joint1 = joints[0]
#     joint2 = joints[1]
#     joint3 = joints[2]

#     M = np.array([[1, 0, 0, link3x + link4x],  # link3x and link4x are along the x-axis
#                   [0, 1, 0, 0],                # No displacement along y-axis
#                   [0, 0, 1, link1z + link2z + link3z],  # link1z, link2z, and link3z along z-axis
#                   [0, 0, 0, 1]])

#     # Screw axes (S) for each joint in the space frame
#     S1 = np.array([0, 0, 1, 0, 0, 0])            # Rotation about z-axis
#     S2 = np.array([0, 1, 0, 0, 0, -link1z])      # Rotation about y-axis, negative moment arm along z due to link1z
#     S3 = np.array([1, 0, 0, 0, -link3z, 0])

#     # Convert joint angles from degrees to radians
#     theta1 = joints[0] * np.pi / 180
#     theta2 = joints[1] * np.pi / 180
#     theta3 = joints[2] * np.pi / 180
#     # thetas = [theta1, theta2, theta3]
#     thetas = [joint1, joint2, joint3]

#     # Compute the exponential product of the exponentials
#     T = mr.FKinSpace(M, [S1, S2, S3], thetas)
    
#     # Extract the position [x, y, z] from the transformation matrix
#     x = T[0, 3]
#     y = T[1, 3]
#     z = T[2, 3]

#     return [x, y, z]

def skew_symmetric(v):
    """ Returns the skew symmetric matrix of a vector """
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])

def exp_from_twist(axis, theta):
    """ Returns the transformation matrix from a twist (screw axis and angle) """
    omega = np.array(axis[:3])  # angular velocity vector
    v = np.array(axis[3:])  # linear velocity vector
    omega_skew = skew_symmetric(omega)
    I = np.eye(3)
    if np.linalg.norm(omega) == 0:  # pure translation
        R = I
        p = v * theta
    else:  # rotation and possibly a translation
        R = I + np.sin(theta) * omega_skew + (1 - np.cos(theta)) * np.dot(omega_skew, omega_skew)
        p = np.dot(I * theta + (1 - np.cos(theta)) * omega_skew + (theta - np.sin(theta)) * np.dot(omega_skew, omega_skew), v)
    return np.vstack((np.hstack((R, p.reshape(3, 1))), [0, 0, 0, 1]))

def forward_kinematics(joints):
    # Define the screw axes for each joint in the space frame
    S1 = np.array([0, 0, 1, 0, 0, 0])        # Rotation about z-axis
    S2 = np.array([0, 1, 0, -0.065, 0, 0])   # Rotation about y-axis
    S3 = np.array([1, 0, 0, 0, -0.104, 0])   # Rotation about x-axis

    # Initial transformation matrix (identity)
    T = np.eye(4)

    # List of screw axes
    screws = [S1, S2, S3]
    for i, joint in enumerate(joints):
        T = np.dot(T, exp_from_twist(screws[i], joint))  # Multiply with the exp map of the current joint twist

    # Extract the position [x, y, z] from the transformation matrix
    x = T[0, 3]
    y = T[1, 3]
    z = T[2, 3]

    return [x, y, z]

 
