import numpy as np
import matplotlib.pyplot as plt

#EX6
print("EX6")
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.1, 3.5, 4.2, 3.1, 4.4, 6.8])

V = np.vstack([x**3, x**2, x, np.ones_like(x)]).T

a0, a1, a2, a3 = np.linalg.lstsq(V, y, rcond=None)[0]

plt.scatter(x, y)
plt.plot(x ,a0*x**3 + a1*x**2 + a2*x + a3)
plt.xlabel('Time in Days')
plt.ylabel('Grams')
plt.legend()
plt.show()
