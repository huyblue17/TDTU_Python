import math as m
import numpy as np 
import sympy as sp 

#EX1
print("EX1")
def norm(A):
    norm_A = max(np.sum(np.abs(A), axis = 0))
    return norm_A

A1 = [[1, -7], [-2, -3]]
A2 = [[-2, 8], [3, 1]]
A3 = [[2, -8], [3, 1]]
A4 = [[1, -7], [-2, -3]]
A5 = [[5, -4, 2], [-1, 2, 3], [-2, 1, 0]]

print("a. 1-norm A1:", norm(A1))
print("b. 1-norm A2:", norm(A2))
print("c. 1-norm A3:", norm(A3))
print("d. 1-norm A4:", norm(A4))
print("e. 1-norm A5:", norm(A5))