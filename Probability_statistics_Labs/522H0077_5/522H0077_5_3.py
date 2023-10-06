import matplotlib.pyplot as plt
import numpy as np

n_trials = 10
p_success = 0.4
X = np.arange(1, 11)

P = np.array([np.math.comb(n_trials, k-1) * p_success**(k-1) * (1-p_success)**(n_trials-k+1) for k in X])

plt.plot(X, P, 'o', label='Points', color='b')
plt.plot(X, P, '-', label='Lines', color='b')
plt.title("Probability of Hitting the Target on the K-th Try")
plt.xlabel("K")
plt.ylabel("Probability")
plt.xticks(X)
plt.legend()
plt.show()