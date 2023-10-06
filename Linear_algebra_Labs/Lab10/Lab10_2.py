import numpy as np
import matplotlib.pyplot as plt

#EX2
print("EX2")
A = np.array([[-6, 28, 21],
              [4, -15, -12],
              [8, 0, 25]])

a_values = [32, 31.9, 31.8, 32.1, 32.2]

fig, ax = plt.subplots()

for a in a_values:
    A[2, 1] = a
    char_poly = np.poly(A)
    t = np.linspace(0, 3, 100)
    p_t = np.polyval(char_poly, t)
    ax.plot(t, p_t, label=f'a = {a}')

ax.set_title('Characteristic Polynomials Graph')
ax.set_xlabel('t')
ax.set_ylabel('p(t)')
ax.legend()
plt.show()
