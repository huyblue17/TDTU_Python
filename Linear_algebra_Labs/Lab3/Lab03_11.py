import numpy as np 
import math as m 

#EX11
print("EX11: ")

A = np.array([[2, 4, 1],
              [6, 7, 2],
              [3, 5, 9]])

if A.shape[0] == A.shape[1]:
    print("a. A is a square matrix")
A1 = A.T
result = np.allclose(A,A1)
if result == False:
    print("b. A is symmetric")
else:
    print("b. A is not symmetric")
result2 = np.allclose(A,-A1)
if result2 == True:
    print("c. A is skew-symmetric")
else:
    print("c. A is not skew-symmetric")
print("d. Upper Triangular: ", np.triu(A,k=0))
print("d. Lower Triangular: ", np.tril(A,k=0))

 