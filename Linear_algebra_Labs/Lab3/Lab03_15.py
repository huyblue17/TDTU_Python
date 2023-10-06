import numpy as np
import math as m

#EX15
print("EX15: ")

A = np.array([[2, 4, 5], 
              [2, -3, 4], 
              [1, 4, 1]])
B = np.array([[1, -1, 2], 
              [3, 4, 3], 
              [2, 1, -2]])


invA = np.linalg.inv(A)
invB = np.linalg.inv(B)

invAB = np.dot(invA,invB)

AB = np.dot(A, B)
invAB2 = np.linalg.inv(AB)


BA = np.dot(B, A)
invBA = np.linalg.inv(BA)

AinvT = np.transpose(invA)

print("A^-1:\n", invA)
print("B^-1:\n", invB)
print("A^-1 * B^-1:\n", invAB)
print("(AB)^-1:\n", invAB2)
print("(BA)^-1:\n", invBA)
print("(A^-1)^T:\n", AinvT)
