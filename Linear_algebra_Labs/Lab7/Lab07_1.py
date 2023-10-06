import numpy as np
import sympy as sp
import math as m 

#EX1
print("EX1.")

v1 = np.array([1, 2, 3, 4])
v2 = np.array([-1, 0, 1, 3])
v3 = np.array([0, 5, -6, 8])
w = np.array([3, -6, 17, 11])

A = np.column_stack((v1, v2, v3))
B = np.column_stack((A, w))

rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

if rank_A == rank_B:
    print("a.v1, v2, v3 are linear combination")
else:
    print("a.v1, v2, v3 are not linear combination")


v1 = np.array([1, 1, 2, 2])
v2 = np.array([2, 3, 5, 6])
v3 = np.array([2, -1, 3, 6])
w = np.array([0, 5, 3, 0])

A = np.column_stack((v1, v2, v3))
B = np.column_stack((A, w))

rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

if rank_A == rank_B:
    print("b.v1, v2, v3 are linear combination")
else:
    print("b.v1, v2, v3 are not linear combination")


v1 = np.array([1, 1, 2, 2])
v2 = np.array([2, 3, 5, 6])
v3 = np.array([2, -1, 3, 6])
w = np.array([-1, 6, 1, -4])

A = np.column_stack((v1, v2, v3))
B = np.column_stack((A, w))

rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

if rank_A == rank_B:
    print("c.v1, v2, v3 are linear combination")
else:
    print("c.v1, v2, v3 are not linear combination")

v1 = np.array([1, 2, 3, 4])
v2 = np.array([-1, 0, 1, 3])
v3 = np.array([0, 5, -6, 8])
v4 = np.array([1, 15, -12, 8])
w = np.array([0, -6, 17, 11])

A = np.column_stack((v1, v2, v3, v4))
B = np.column_stack((A, w))

rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

if rank_A == rank_B:
    print("d.v1, v2, v3 are linear combination")
else:
    print("d.v1, v2, v3 are not linear combination")
