import numpy as np

#EX5
print("EX5")
#A1
A1 = np.array([[4, -5],
               [2, -3]])

#A2
A2 = np.array([[0, 2],
               [0, 1]])

#A3
A3 = np.array([[2, 3],
               [1, 4]])

#A4
A4 = np.array([[1, 2, -2],
               [-2, 5, -2],
               [-6, 6, -3]])

#A5
A5 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]])

# Hàm kiểm tra chéo hóa
def is_diagonalizable(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return np.allclose(matrix, np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors)))

#Kiểm tra ma trận
matrices = [A1, A2, A3, A4, A5]
for i, matrix in enumerate(matrices):
    if is_diagonalizable(matrix):
        print(f"Matrix A{i+1} is diagonalizable")
    else:
        print(f"Matrix A{i+1} is not diagonalizable")
