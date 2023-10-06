import math as m 
import numpy as np 
import sympy as sp 

#EX6
print("EX6")
def sat(v,s):
    dis = np.linalg.norm(v - s) 
    return dis

v =  np.array([1, 2, 3])
s1 = np.array([7, 4, 3])
s2 = np.array([2, 1, 9])

print("Distance bet v and s2: ",sat(v,s1))
print("Distance bet v and s3: ",sat(v,s2))
print("Distance bet s2 and s3: ",sat(s1,s2))