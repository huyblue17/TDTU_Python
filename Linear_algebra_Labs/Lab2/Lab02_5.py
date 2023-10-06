import numpy as np 
import math as m

#EX5
print("EX5: ")
Y = np.array([[1, 2, 16, 31, 22],    
              [2, 8, 12, 21, 23],
              [4, 9, 11, 14, 25],
              [3, 6, 10, 16, 34]])

x = Y[1,1:4]
y = Y[:,2]
y = y.reshape(-1,1)
mA = Y[1:3 , 1:4]
mB = Y[:, 0::2]
mC = Y[1:4, [0, 2, 3, 4]]
mD = Y[Y>12]
mDD = np.reshape(mD,(3,3)) 

print("a. x =", x)
print("a. y =", y)
print("c. A =", mA)
print("d. B =", mB)
print("e. Matrix C =", mC)
print("f. Matrix D =", mDD)

