import math as m
import numpy as np 
import sympy as sp

#EX4
print("EX4")
def cos0(u,v):
    u_n = np.linalg.norm(u)
    v_n = np.linalg.norm(v)
    dot_uv = np.dot(u,v)
    cos_0 = dot_uv / (v_n * u_n)
    acos0 = m.acos(cos_0)
    deg = round(m.degrees(acos0))
    return deg

u1 = [1, 1]
v1 = [0, 1]

u2 = [1, 0]
v2 = [0, 1]

u3 = [-2, 3]
v3 = [1/2, -1/2]

print("a. Degree between 2 vec: ", cos0(u1,v1))
print("b. Degree between 2 vec: ", cos0(u2,v2))
print("c. Degree between 2 vec: ", cos0(u3,v3))
