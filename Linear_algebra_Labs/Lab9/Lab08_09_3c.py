import numpy as np
import matplotlib.pyplot as plt

#EX3
print("EX3")
#c
x = np.array([-1, 0, 1, 2])
y = np.array([0, 1, 2, 4])

C = np.vstack([x, np.ones(len(x))]).T

c0, c1 = np.linalg.lstsq(C, y, rcond=None)[0]

print("c.")
plt.scatter([-1, 0, 1, 2], [0, 1, 2, 4])
plt.plot(x, c0*x + c1)
plt.show()



