import numpy as np

#EX14
print("EX14: ")


for n in [2, 3, 4]:
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    det_AB = np.linalg.det(A.dot(B))
    det_A_det_B = np.linalg.det(A) * np.linalg.det(B)
    print(f"The determinant of AB is {det_AB}")
    print(f"The product of the determinants of A and B is {det_A_det_B}")

