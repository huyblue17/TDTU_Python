import pandas as pd

# Read iris.csv
df = pd.read_csv("iris.csv")

# Show the first 5 data points
print(df.head(5))

# Compute count, mean, std, min, and max for numerical columns
numeric_columns = df.select_dtypes(include=['float64'])
count = numeric_columns.shape[0]
mean = numeric_columns.mean()
std = numeric_columns.std()
min_values = numeric_columns.min()
max_values = numeric_columns.max()

# Create DataFrame for the statistics
results = pd.DataFrame({"Count": count,
                        "Mean": mean,
                        "Std": std,
                        "Min": min_values,
                        "Max": max_values})

# Transpose the DataFrame
results = results.transpose()

print("\nDataframe:")
print(results)