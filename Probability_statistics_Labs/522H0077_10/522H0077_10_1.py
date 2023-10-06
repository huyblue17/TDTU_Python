import random
import matplotlib.pyplot as plt
import numpy as np


num_rolls = 10000
x = [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_rolls)]

X = list(set(x))
X.sort()


P = [x.count(value) / num_rolls for value in X]


expectation = sum(X[i] * P[i] for i in range(len(X)))
variance = sum((X[i] - expectation) ** 2 * P[i] for i in range(len(X)))
standard_deviation = np.sqrt(variance)

print("X values:", X)
print("Probability distribution:", P)
print("Expectation:", expectation)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
plt.bar(X, P)
plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Probability Distribution of X')
plt.show()
