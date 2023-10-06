import numpy as np 
import math as m 

#EX1
print("EX1: ")
x = np.arange(1, 6, 1)
b = np.arange(1, 7, 1)
c = np.arange(1, 31)
d = np.arange(1, 26)

print("Matrix A: ")
A = np.tile(x,(5,1))
A1 =A.T
print(A1)

print("Matrix B: ")
B = np.tile(b,(6,1))
print(B)

print("Matrix C: ")
C = np.reshape(c,(6,5))
C1 = C.T
print(C1)

print("Matrix D: ")
D = np.reshape(d,(5,5))
print(D)

