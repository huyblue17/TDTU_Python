import math as m 
import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt 

#EX2
print("EX2")
def plot2Dgraph(x, a, b, c):
    if b != 0:
        f1 = lambda x: (c - a*x) / b
        y = list(map(f1, x))
        plt.plot(x, y)
    elif a != 0:
        x = [c/a] * len(x)
        y = np.linspace(min(x), max(x), len(x))
        plt.plot(x, y)
    else:
        print("Cant draw the graph")
#sys1: x + y = 0, x - y =2
#sys2: x + y = 5, 2x + 2y =12
#sys3: x + y = 5, 3x+ 3y = 15
#sys1: x = 0, x - y = 2

x = np.linspace(-10, 10, 100)

a1 ,b1 ,c1 = 1, 1, 0
a2, b2, c2 = 1, -1, 2

plt.title('Graph')

plot2Dgraph(x, a1, b1, c1)
plot2Dgraph(x, a2, b2, c2)

plt.legend()
plt.show()

