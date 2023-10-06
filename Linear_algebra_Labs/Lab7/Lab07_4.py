import numpy as np 
import sympy as sp
import math as m 

#EX4
print("EX4")

A = np.array([[1, 0, 2, 3],
              [4, -1, 0, 2],
              [0, 1, -8, -10]])
A2 = sp.Matrix(A).nullspace()

nullspace = np.hstack(A2)

print(nullspace)
print("a.1 ", v1)
print("a.2 ", v2)