import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('company-sales_data.csv')
months = data['month_number']
toothpaste = data['toothpaste']
shampoo = data['shampoo']
facecream = data['facecream']

plt.figure(figsize=(10, 6))
plt.plot(months, toothpaste, marker='o', label='Toothpaste')
plt.plot(months, shampoo, marker='o', label='Shampoo')
plt.plot(months, facecream, marker='o', label='Face Cream')

plt.title('Monthly Sales of Toothpaste, Shampoo, and Face Cream')
plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.xticks(months)
plt.grid(True)
plt.legend()
plt.show()
