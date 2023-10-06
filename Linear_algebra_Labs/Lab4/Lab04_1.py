import math as m
import numpy as np
import sympy as sp

#EX1
print("EX1")
#a
A = np.array([[1, 2, 1], [2, -1, 1], [2, 1, 0]])
C1 = np.array([0, 0, 0])

#Cach 1
X1 = np.linalg.solve(A,C1)
#Cach 2
A1 = np.linalg.inv(A)
X2 = np.matmul(C1,A1)
#Cach 3
A,C1 = sp.symbols('A, C1')
eq1a = sp.Eq(A + C1, 0)
eq2a = sp.Eq(A - C1, 2)
X3 = sp.solve((eq1a,eq2a),(A,C1))

print("A. Cach 1", X1)
print(" . Cach 2", X2)
print(" . Cach 3", X3)

print(f"X = {X1[0]:.2f}")
print(f"X = {X1[1]:.2f}")
print(f"X = {X1[2]:.2f}")

#b
B = np.array([[2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 2], [1, 1, 1, 2]])
C2 = np.array([1, 1, 1, 1])

#Cach 1
Xb1 = np.linalg.solve(B,C2)
#Cach 2
B1 = np.linalg.inv(B)
Xb2 = np.matmul(C2,B1)
#Cach 3
x, y, t, z = sp.symbols('x y t z')
eq1b = sp.Eq(2*x + y + z + t, 1)
eq2b = sp.Eq(x + 2*y + z + t, 1)
eq3b = sp.Eq(x + y + 2*z + 2*t, 1)
eq4b = sp.Eq(x + y + z + 2*t, 1)
Xb3 = sp.solve((eq1b,eq2b,eq3b,eq4b),(x, y, z, t))

print("B. Cach 1", Xb1)
print(" . Cach 2", Xb2)
print(" . Cach 3", Xb3)

print(f"x = {Xb1[0]:.2f}")
print(f"y = {Xb1[1]:.2f}")
print(f"z = {Xb1[2]:.2f}")
print(f"t = {Xb1[3]:.2f}")