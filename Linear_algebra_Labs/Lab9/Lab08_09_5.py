import numpy as np
import matplotlib.pyplot as plt

#EX5
print("EX5")
A = np.array([[np.cos(1), np.sin(1)], [np.cos(2), np.sin(2)], [np.cos(3), np.sin(3)]])
b = np.array([7.9, 5.4, -9])

A, B = np.linalg.lstsq(A, b, rcond=None)[0]

plt.scatter(x, y)
plt.plot(x, A*np.cos(x) + B*np.sin(x))
plt.show()