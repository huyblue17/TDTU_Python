import numpy as np

#EX4
print("EX4")
A = np.array([[-2, 2, -3],
              [2, 1, -6],
              [-1, -2, 0]])

eigenvalues_A, eigenvectors_A = np.linalg.eig(A)

# transpose of A
eigenvalues_AT, eigenvectors_AT = np.linalg.eig(A.T)

# inverse of A
eigenvalues_A_inv, eigenvectors_A_inv = np.linalg.eig(np.linalg.inv(A))

#A
print("Eigenvalues of A:")
for eigenvalue in eigenvalues_A:
    print(eigenvalue)

print("\nEigenvectors of A:")
for i in range(len(eigenvectors_A)):
    eigenvalue = eigenvalues_A[i]
    eigenvector = eigenvectors_A[:, i]
    print(f"Eigenvalue {eigenvalue}:")
    print(eigenvector)
    print()

#AT 
print("Eigenvalues of AT:")
for eigenvalue in eigenvalues_AT:
    print(eigenvalue)

print("\nEigenvectors of AT:")
for i in range(len(eigenvectors_AT)):
    eigenvalue = eigenvalues_AT[i]
    eigenvector = eigenvectors_AT[:, i]
    print(f"Eigenvalue {eigenvalue}:")
    print(eigenvector)
    print()

print("Eigenvalues of A-1:")
for eigenvalue in eigenvalues_A_inv:
    print(eigenvalue)

print("\nEigenvectors of A-1:")
for i in range(len(eigenvectors_A_inv)):
    eigenvalue = eigenvalues_A_inv[i]
    eigenvector = eigenvectors_A_inv[:, i]
    print(f"Eigenvalue {eigenvalue}:")
    print(eigenvector)
    print()
