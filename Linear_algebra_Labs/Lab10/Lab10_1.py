import numpy as np

#EX1
print("EX1")
A = np.array([[-1, 3.5, 14], [0, 5, -26], [0, 0, 2]])
B = np.array([[-2, 0, 0], [99, 0, 0], [10, -4.5, 10]])
C = np.array([[5, 5, 0, 2], [0, 2, -3, 6], [0, 0, 3, -2], [0, 0, 0, 5]])
D = np.array([[3, 0, 0, 2], [6, 2, 0, 0], [0, 3, 6, 0], [2, 3, 3, -5]])
E = np.array([[3, 0, 0, 0, 0], [-5, 1, 0, 0, 0], [3, 8, 0, 0, 0], [0, -7, 2, 1, 0], [-4, 1, 9, -2, 3]])

eigenvalues_A, a = np.linalg.eig(A)
eigenvalues_B, b = np.linalg.eig(B)
eigenvalues_C, c = np.linalg.eig(C)
eigenvalues_D, d = np.linalg.eig(D)
eigenvalues_E, e = np.linalg.eig(E)

print("Eigenvalues of A:")
print(eigenvalues_A)

print("Eigenvalues of B:")
print(eigenvalues_B)

print("Eigenvalues of C:")
print(eigenvalues_C)

print("Eigenvalues of D:")
print(eigenvalues_D)

print("Eigenvalues of E:")
print(eigenvalues_E)