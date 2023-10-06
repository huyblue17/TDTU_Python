import numpy as np

#EX7
print("EX7")
#A1
A1 = np.array([[1, 0],
               [0, -3]])

#A2
A2 = np.array([[-5, 0],
               [0, 0]])

#A3
A3 = np.array([[np.sqrt(6), 1],
               [0, np.sqrt(6)]])

#A4
A4 = np.array([[np.sqrt(3), 2],
               [0, np.sqrt(3)]])

#singular values of A1
U1, S1, VT1 = np.linalg.svd(A1)
print("Singular values of A1:")
print(S1)

#singular values of A2
U2, S2, VT2 = np.linalg.svd(A2)
print("Singular values of A2:")
print(S2)

#singular values of A3
U3, S3, VT3 = np.linalg.svd(A3)
print("Singular values of A3:")
print(S3)

#singular values of A4
U4, S4, VT4 = np.linalg.svd(A4)
print("Singular values of A4:")
print(S4)
