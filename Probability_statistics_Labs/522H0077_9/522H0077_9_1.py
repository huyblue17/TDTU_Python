import pandas as pd
import matplotlib.pyplot as plt

iris_df = pd.read_csv('iris.csv')
sepal_length = iris_df['sepal_length']
sepal_width = iris_df['sepal_width']

plt.figure(figsize=(8, 6))
plt.scatter(sepal_length, sepal_width, c='r', marker='o', label='Data Points')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(sepal_length, bins=20, edgecolor='blue', alpha=0.7)
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.grid()
plt.show()
