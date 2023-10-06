import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def pmf_normal(x, mu, sigma):
    return norm.pdf(x, mu, sigma)

def cdf_normal(x, mu, sigma):
    return norm.cdf(x, mu, sigma)


mu = 3
sigma = 4

x_values = np.linspace(-10, 16, 400)
pmf_values = pmf_normal(x_values, mu, sigma)
cdf_values = cdf_normal(x_values, mu, sigma)

plt.figure(figsize=(10, 6))
plt.plot(x_values, pmf_values, label='PMF (Normal Distribution)')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.title('Probability Mass Function of Normal Distribution')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(x_values, cdf_values, label='CDF (Normal Distribution)')
plt.xlabel('X')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function of Normal Distribution')
plt.legend()
plt.grid(True)
plt.show()

p_between_2_and_7 = cdf_normal(7, mu, sigma) - cdf_normal(2, mu, sigma)
print(f"P(2 < X < 7) = {p_between_2_and_7:.4f}")
