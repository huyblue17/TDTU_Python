import numpy as np

#EX8
print("EX8")
def R(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
trans = np.array([[1, 0], [0, 1]]).T

print("a.")
theta_a = np.pi
R_a = R(theta_a)
result_a = np.dot(R_a, trans)
print(result_a)

print("b.")
theta_b = np.pi/3
R_b = R(theta_b)
result_b = np.dot(R_b, trans)
print(result_b)
