import numpy as np
import matplotlib.pyplot as plt

#EX3
print("EX3")
#a
x = np.array([0, 1, 2, 3])
y = np.array([1, 1, 2, 2])

A = np.vstack(x, np.ones(len(x)))[1]

a0, a1 = np.linalg.lstsq(A, y, rcond=None)[0]

print("a.")
plt.scatter([0, 1, 2, 3], [1, 1, 2, 2])
plt.plot(x, a0*x + a1)
plt.show()


