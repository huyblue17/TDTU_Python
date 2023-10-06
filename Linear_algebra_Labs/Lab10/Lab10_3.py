import numpy as np

#EX3
print("EX3")
M = np.array([[-3, -5, -7],
              [-2, 1, 0],
              [1, 5, 5]])

eigenvalues, eigenvectors = np.linalg.eig(M)

#a
print("a. Eigenvalues:")
for eigenvalue in eigenvalues:
    print(eigenvalue)

#b
print("\nb. Eigenvectors:")
for i in range(len(eigenvectors)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]
    print(f"Eigenvalue {eigenvalue}:")
    print(eigenvector)
    print()
