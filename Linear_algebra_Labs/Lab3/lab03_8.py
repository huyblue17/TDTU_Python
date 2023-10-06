import numpy as np 
import math as m 


#EX8
print("EX8: ")
mS = np.array([[12, 15, 10, 16, 12],   # Strawberry
               [5, 9, 14, 7, 10],      # Vanilla
               [8, 12, 10, 9, 15]])    #Chocolate  
mSs = mS.T
price = np.array([2, 1, 3])

total = np.matmul(mSs,price)
print("Total sale from Mon to Fri: " ,total)