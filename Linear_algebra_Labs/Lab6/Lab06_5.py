import math as m 
import numpy as np 
import sympy as sp 

#EX5
print("EX5")
def unit_v(u):
    u_n = np.linalg.norm(u)
    Uu = u / u_n
    return Uu

u1 = [2, 3]
u2 = [1, 2, 3]
u3 = [1/2, -1/2 , 1/4]
u4 = [m.sqrt(2), 2, -m.sqrt(2)]

print("a. Unit of vector u", unit_v(u1))
print("b. Unit of vector u", unit_v(u2))
print("c. Unit of vector u", unit_v(u3))
print("d. Unit of vector u", unit_v(u4))