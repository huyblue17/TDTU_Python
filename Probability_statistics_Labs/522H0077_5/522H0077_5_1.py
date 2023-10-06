import matplotlib.pyplot as plt
import numpy as np

n_machines = 5
p_broken = 0.1

X = np.arange(0, n_machines+1)
P = np.array([np.math.comb(n_machines, k) * p_broken**k * (1-p_broken)**(n_machines-k) for k in X])

plt.plot(X, P, 'o-', color='b')
plt.title("Probability Distribution Function")
plt.xlabel("Number of Broken Machines")
plt.ylabel("Probability")
plt.xticks(X)
plt.show()