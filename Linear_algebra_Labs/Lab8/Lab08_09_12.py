import numpy as np
import matplotlib.pyplot as plt


x = np.array([2015, 2016, 2017, 2018, 2019])
y = np.array([12, 19, 29, 37, 45])

n = len(x)
m = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x**2) - np.sum(x)**2)
b = (np.sum(y) - m*np.sum(x)) / n

x_pred = 2020

y_pred = m*x_pred + b

plt.scatter(x, y, color='blue')
plt.plot(x, m*x + b, color='red')
plt.scatter(x_pred, y_pred, color='black')
plt.xlabel('Year')
plt.ylabel('Sales (in million dollars)')
plt.title('Sales of a Company')
plt.show()
print("Estimated sales in 2020: ")
