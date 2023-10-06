import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#EX1
def plot_cdf_normal(mu, sigma):
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000) # generate x-values
    y = norm.cdf(x, mu, sigma) # generate y-values (cumulative probabilities)
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Cumulative Probability')
    plt.title('Cumulative Distribution Function of Normal({}, {})'.format(mu, sigma))
    plt.show()

# Example usage
plot_cdf_normal(0, 1.5)
