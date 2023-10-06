import numpy as np
import matplotlib.pyplot as plt

#EX10
print("EX10")
P = np.array([1, 1])
Q = np.array([3, 1])
R = np.array([1, 3])

A = np.column_stack((P, Q, R))

n = A.shape[0]
I = np.identity(n)
neg_I = -1 * I
new_A = neg_I @ A

P_new = new_A[:, 0]
Q_new = new_A[:, 1]
R_new = new_A[:, 2]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))


ax1.set_title("Original")
ax1.plot([P[0], Q[0]], [P[1], Q[1]], 'b-', label='PQ')
ax1.plot([Q[0], R[0]], [Q[1], R[1]], 'b-', label='QR')
ax1.plot([R[0], P[0]], [R[1], P[1]], 'b-', label='RP')
ax1.plot(P[0], P[1], 'ro', label='P')
ax1.plot(Q[0], Q[1], 'ro', label='Q')
ax1.plot(R[0], R[1], 'ro', label='R')
ax1.legend()

ax1.set_title("New")
ax2.plot([P_new[0], Q_new[0]], [P_new[1], Q_new[1]], 'r-', label='P\'Q\'')
ax2.plot([Q_new[0], R_new[0]], [Q_new[1], R_new[1]], 'r-', label='Q\'R\'')
ax2.plot([R_new[0], P_new[0]], [R_new[1], P_new[1]], 'r-', label='R\'P\'')
ax2.plot(P_new[0], P_new[1], 'bo', label='P\'')
ax2.plot(Q_new[0], Q_new[1], 'bo', label='Q\'')
ax2.plot(R_new[0], R_new[1], 'bo', label='R\'')
ax2.legend()

plt.show()
