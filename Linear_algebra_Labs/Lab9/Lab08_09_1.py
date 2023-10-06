import numpy as np 

#EX1
print("EX1")
A = np.array([[2, 2], [2, 3]])

b = np.array([[4], [6]])

x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
print("Least square solution: x = ",x[0], "y = ",x[1])