import numpy as np 
import math as m 

#EX9
print("EX9: ")
T = np.array([[0.6, 0.7],
              [0.4, 0.3]])

p = np.array([[0.5] , [0.5]])

for k in [1, 2, 10, 100, 100000]:
    pk = p
    for i in range (k):
        pk = np.matmul(pk, T)
    print(f"p{k} = {pk}")
