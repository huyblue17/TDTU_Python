import math as m 
import numpy as np 
import sympy as sp 

#EX7
print("EX7")
A = np.array([[1, 2, 3],
              [2, 1, 2],
              [3, 2, 4]])
A_inv = np.linalg.inv(A)
E = np.array([[80, 98, 99, 85, 106, 94],
              [71, 92, 76, 95, 100, 92],
              [124, 163, 140, 160, 176, 161]])
D = np.matmul(A_inv, E)

print(D)
for column in D:
    for ele in row:
        r_ele = round(ele)
        if(r_ele == 30):
            print(" ", end = " ")
        else:
            print(chr(int(r_ele)+61), end= "")
