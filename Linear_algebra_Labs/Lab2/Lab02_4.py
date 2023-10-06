import numpy as np 
import math as m 

#EX3
print("EX3: ")
a = np.arange(1,10)
A = np.reshape(a,(3,3))
print("Matrix A: ")
print(A)
B = np.flip(A, axis = 0)
print("Matrix B: ")
print(B)