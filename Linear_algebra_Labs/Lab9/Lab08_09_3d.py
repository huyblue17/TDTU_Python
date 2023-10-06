import numpy as np
import matplotlib.pyplot as plt

#EX3
print("EX3")
#d
x = np.array([2, 3, 5, 6])
y = np.array([3, 2, 1, 0])

D = np.vstack([x, np.ones(len(x))]).T

d0, d1 = np.linalg.lstsq(D, y, rcond=None)[0]

print("d.")
plt.scatter([2, 3, 5, 6], [3, 2, 1, 0])
plt.plot(x, d0*x + d1)
plt.show()




