import numpy as np 
import math as m 

#EX12
print("EX12: ")
A = np.array([[6, 0, 0, 5],
              [1, 7, 2, -5],
              [2, 0, 0, 0],
              [8, 3, 1, 8]])
dA = np.linalg.det(A)
print("A.", round(dA, 0))

B = np.array([[1, -2, 5, 2],
              [0, 0, 3, 0],
              [2, -6, -7, 5],
              [5, 0, 4, 4]])
dB = np.linalg.det(B)
print("B. ", round(dB, 0))

C = np.array([[3, 5, -8, 4],
              [0, -2, 3, -7],
              [0, 0, 1, 5],
              [0, 0, 0, 2]])
dC = np.linalg.det(C)
print("C. ", round(dC, 0))

D = np.array([[4, 0, 0, 0],
              [7, -1, 0, 0],
              [2, 6, 3, 0],
              [5, -8, 3, 0],
              [5, -8, 4, -3]])

#dD = np.linalg.det(D)
#print(round(dD, 0))

E = np.array([[4, 0, -7, 3, -5],
              [0, 0, 2, 0, 0],
              [7, 3, -6, 4, -8],
              [5, 0, 5, 2, -3],
              [0, 0, 9, -1, 2]])
dE = np.linalg.det(E)
print("E. ", round(dE, 0))

F = np.array([[6, 3, 2, 4, 0],
              [9, 0, -4, 1, 0],
              [8, -5, 6, 7, 1],
              [3, 0, 0, 0, 0],
              [4, 2, 3, 2, 0]])
dF = np.linalg.det(F)
print("F. ", round(dF, 0))
