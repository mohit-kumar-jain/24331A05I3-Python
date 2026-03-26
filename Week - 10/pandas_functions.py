import pandas as pd

df = pd.read_csv('student_performance_dataset.csv')

print("First 5 rows of the dataset:")
print(df.head())

print("\nLast 5 rows of the dataset:")
print(df.tail())

print("\nDataFrame Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe())