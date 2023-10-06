import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('company_sales_data.csv')

# Task 1: Read total profit of all months and use a line plot to show it
months = data['month_number']
total_profit = data['total_profit']

plt.figure(figsize=(10, 6))
plt.plot(months, total_profit, marker='o', color='b')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.title('Total Profit of All Months')
plt.grid()
plt.xticks(months)
plt.show()

# Task 2: Read all month of toothpaste sales data and show it using a scatter plot
toothpaste_sales = data['toothpaste']

plt.figure(figsize=(8, 6))
plt.scatter(months, toothpaste_sales, c='r', marker='x')
plt.xlabel('Month')
plt.ylabel('Toothpaste Sales')
plt.title('Toothpaste Sales of All Months')
plt.grid()
plt.xticks(months)
plt.show()

# Task 3: Read facecream and facewash product and use a bar chart to show them
facecream_sales = data['facecream']
facewash_sales = data['facewash']

plt.figure(figsize=(8, 6))
bar_width = 0.35
bar_positions = months

plt.bar(bar_positions - bar_width/2, facecream_sales, bar_width, label='Face Cream', color='orange')
plt.bar(bar_positions + bar_width/2, facewash_sales, bar_width, label='Face Wash', color='blue')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Face Cream and Face Wash Sales of All Months')
plt.grid()
plt.xticks(bar_positions)
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(facecream_sales, bins=20, edgecolor='blue', alpha=0.7)
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.grid()
plt.show()