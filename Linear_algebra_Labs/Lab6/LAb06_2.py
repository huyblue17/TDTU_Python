import math as m
import numpy as np 
import sympy as sp

#EX2
print("EX2")
def norm(B):
    norm_B = max(np.sum(np.abs(B), axis = 1))
    return norm_B

B1 = [[1, -7], [-2, -3]]
B2 = [[3, 6], [1, 0]]
B3 = [[5, -4, 2], [-1, 2, 3], [-2, 1, 0]]
B4 = [[3, 6, -1], [3, 1, 0], [2, 4, -7]]
B5 = [[-3, 0, 0], [0, 4, 0], [0, 0, 2]]

print("a. infinity-norm B1:", norm(B1))
print("b. infinity-norm B2:", norm(B2))
print("c. infinity-norm B3:", norm(B3))
print("d. infinity-norm B4:", norm(B4))
print("e. infinity-norm B5:", norm(B5))