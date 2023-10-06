import math as m
import numpy as np 
import sympy as sp

#EX2
print("EX2")
def norm(C):
    norm_C = max(sum(np.abs(C)**2))
    return norm_C

C1 = [[5, 4, -2], [-1, 2, 3], [-2, 1, 0]]
C2 = [[1, 7, 3], [4, -2, -2], [-2, -1, 1]]
C3 = [[2, 3], [1, -1]]

print("a. frobenius-norm C1:", norm(C1))
print("b. frobenius-norm C2:", norm(C2))
print("c. frobenius-norm C3:", norm(C3))
