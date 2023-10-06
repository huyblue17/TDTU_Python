import numpy as np 
import sympy as sp
import math as m 

#EX3
print("EX3")
C = np.array([[1, 0, 2, 3],
              [4, -1, 0, 2],
              [0, -1, -8, -10]])

#a
mat_C = sp.Matrix(C).rref()
print("a.Basic col of C", mat_C[1])
print(C[:, mat_C[1]])

#b
C_T = C.T 
mat_CT = sp.Matrix(C_T).rref()
print("b.Basic row of C", mat_CT[1])
print(C_T[mat_CT[1] ,:])
