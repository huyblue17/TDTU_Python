import numpy as np
import sympy as sp
import math as m 

#EX2
print("EX2.")
#a
A = np.column_stack(([1, 0, 2], [0, 1, 4], [1, -1, 1]))
mat_A = sp.Matrix(A).rref()

if len(mat_A[1]) == len([1, 0, 2]):
    print("a.v1, v2, v3 are linearly independent")
else:
    print("a.v1, v2, v3 are not linearly independent")

#d
D = np.column_stack(([0, 0, 1, 2, 3], [0, 0, 2, 3, 1], [1, 2, 3, 4, 5], [2, 1, 0, 0, 0], [-1, -3, -5, 0, 0]))
mat_D = sp.Matrix(D).rref()

if len(mat_D[1]) == len([0, 0, 1, 2, 3]):
    print("d.v1, v2, v3, v4 and v5 are linearly independent")
else:
    print("d.v1, v2, v3, v4 and v5 are not linearly independent") 
