import numpy as np
from collections import Counter

x = [0, 5, 2, 3, 1, 4, 2, 6, 2, 3] 

X = np.unique(x)

P = []
counter = Counter(x)
for i in X:
    P.append(counter[i] / len(x))

expectation = np.sum(X * P)
variance = np.sum((X - expectation) ** 2 * P)
std_dev = np.sqrt(variance)


P_3_or_more = np.sum(np.array(P)[X >= 3])


print("X :", X)
print("P :", P)
print("Expectation :", expectation)
print("Variance :", variance)
print("Standard deviation :", std_dev)
print("P(3 or more) :", P_3_or_more)