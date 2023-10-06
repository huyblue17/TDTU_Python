import matplotlib.pyplot as plt
import numpy as np

mean_calls = 3
X = np.arange(1, 6)

P = np.array([np.exp(-mean_calls) * mean_calls**k / np.math.factorial(k) for k in X])

plt.plot(X, P, 'o', label='Points', color='b')
plt.plot(X, P, '-', label='Lines', color='b')
plt.title("Probability of Receiving K Phone Calls in 1 Minute")
plt.xlabel("Number of Phone Calls (K)")
plt.ylabel("Probability")
plt.xticks(X)
plt.legend()
plt.show()