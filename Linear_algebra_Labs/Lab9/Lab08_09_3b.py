import numpy as np
import matplotlib.pyplot as plt

#EX3
print("EX3")
#b
x = np.array([1, 2, 4, 5])
y = np.array([0, 1, 2, 3])

B = np.vstack([x, np.ones(len(x))]).T

b0, b1 = np.linalg.lstsq(B, y, rcond=None)[0]

print("b.")
plt.scatter([1, 2, 4, 5], [0, 1, 2, 3])
plt.plot(x, b0*x + b1)
plt.show()


