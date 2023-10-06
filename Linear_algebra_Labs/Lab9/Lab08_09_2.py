import numpy as np

#EX2
print("EX2")
A = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 2, 1],
              [1, 0, 1],
              [4, 1, 1],
              [4, 2, 1]])

b = np.array([[0.5],
              [1.6],
              [2.8],
              [0.8],
              [5.1],
              [5.9]])

x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)


print("Least squares: c = ", x[0][0], "d = ", x[1][0], "e = ", x[2][0])