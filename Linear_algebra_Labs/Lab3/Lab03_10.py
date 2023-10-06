import numpy as np 
import math as m 

#EX1
print("EX10: ")

A = np.array([[-1, 4, 8],
              [-9, 1, 2]])
B = np.array([[5, 8],
              [0, -6],
              [5, 6]])
C = np.array([[-4, 1],
              [6, 5]])
D = np.array([[-6, 3, 1],
              [8, 9, -2],
              [6, -1, 5]])

A1 = A.T
B1 = B.T
C1 = C.T
D1 = D.T
#a = np.matmul(A,B1)
b = np.matmul(B,C1)
c = (C-C1)
d = (D-D1)
e = (D1.T)
f = 2*C1
g = (A1+B)
h = (A1+B).T
i = ((2*A1)-(5*B)).T
j = ((-D).T)
k = -(D1)
l = (np.matmul(C,C).T)
m1 = (np.matmul(C1,C1))

#print("a. ", a)
print("b. ", b)
print("c. ", c)
print("d. ", d)
print("e. ", e)
print("f. ", f)
print("g. ", g)
print("h. ", h)
print("i. ", i)
print("j. ", j)
print("k. ", k)
print("l. ", l)
print("m. ", m1)


