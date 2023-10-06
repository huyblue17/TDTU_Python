import numpy as np

#EX6
print("EX6")
A = np.array([[1, 2, -2], [0, 3, -2], [0, 0, 1]])

eigenvals, eigenvectors = np.linalg.eig(A)

P = eigenvectors
P_p = np.linalg.inv(P)
A_P = np.dot(A, P)
D = np.dot(np.dot(P_p, A), P)

# Print matrices A, P, A*P
print("Matrix A:\n", A)
print("Matrix P:\n", P)
print("Matrix A*P:\n", A_P)