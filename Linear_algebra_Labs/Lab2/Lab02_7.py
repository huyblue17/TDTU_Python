import numpy as np 
import math as m 

#EX7
print("EX7: ")
mA = np.array([[2, 7, 9, 7],
               [3, 1, 5, 6],
               [8, 1, 2, 5]])

B = mA[:, 1::2]
C = mA[0::2,:]
print("a.Columms of A into Vec B: ",B)
print("b.Rows of A into Vec C: ", C)
print("c.Convert A into 4x3: ", mA.T)




