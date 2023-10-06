import numpy as np
import matplotlib.pyplot as plt

#EX4
print("EX4")

x_mileage = np.array([2000, 6000, 20000, 30000, 40000])
y_frictionindex = np.array([20, 18, 10, 6, 2])

A = np.vstack([x_mileage, np.ones(len(x))]).T

a0, a1 = np.linalg.lstsq(A, y_frictionindex, rcond=None)[0]

plt.scatter([2000, 6000, 20000, 30000, 40000], [20, 18, 10, 6, 2])
plt.plot(x, a0*x + a1)
plt.show()




