import pandas as pd

# Read population.csv
df = pd.read_csv("population.csv")

# Show the first 5 data points
print(df.head(5))

# Compute statistics by year
grouped_by_year = df.groupby('Year')['Value'].agg(['count', 'mean', 'std', 'min', 'max'])

# Display the results
print("Statistics by Year:")
print(grouped_by_year)

