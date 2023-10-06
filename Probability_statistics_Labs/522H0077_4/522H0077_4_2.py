import numpy as np
from collections import Counter

x = np.random.randint(0, 2, size=(10000, 2))
x_sum = np.sum(x, axis=1)

X = np.unique(x_sum)

P = []
counter = Counter(x_sum)
for i in X:
    P.append(counter[i] / len(x_sum))

expectation = np.sum(X * P)
variance = np.sum((X - expectation) ** 2 * P)
std_dev = np.sqrt(variance)

P_at_least_one_head = np.sum(np.array(P)[X >= 1])


print("X :", X)
print("P :", P)
print("Expectation :", expectation)
print("Variance :", variance)
print("Standard deviation :", std_dev)
print("P(at least one head) :", P_at_least_one_head)