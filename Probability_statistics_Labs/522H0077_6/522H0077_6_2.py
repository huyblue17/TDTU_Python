import numpy as np
from scipy.stats import norm

#EX2
def cdf_normal(x, mu, sigma):
    return norm.cdf(x, loc=mu, scale=sigma)

mu = 10
sigma = 1
lower_bound = 9
upper_bound = 12

prob = cdf_normal(upper_bound, mu, sigma) - cdf_normal(lower_bound, mu, sigma)
print("The period from 9 minutes to 12 minutes is:", prob)