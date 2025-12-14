import seaborn as sns
import pandas as pd

# Load the Iris dataset
df = sns.load_dataset("iris")

# Show first few rows
print(df.head())

# Descriptive statistics for all numeric columns
print("\nDescriptive Statistics using describe():")
print(df.describe())

# Calculate mean, median, min, max, std for each numeric column
numeric_columns = df.select_dtypes(include='number').columns

for col in numeric_columns:
    print(f"\nStatistics for '{col}':")
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Standard Deviation:", df[col].std())



 

# Check for missing values in each column
missing_values = df.isnull().sum()

print("Missing values in each column:")
print(missing_values)
