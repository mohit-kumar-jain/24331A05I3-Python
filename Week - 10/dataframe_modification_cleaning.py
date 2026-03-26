import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', np.nan],
    'Age': [25, 30, 35, 25, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'London'],
    'Salary': ['50000', '60000', '70000', '50000', 'invalid']
}

df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

df['Name'] = df['Name'].fillna('Unknown')

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

df['Age_Group'] = np.where(df['Age'] < 30, 'Young', 'Adult')

df.rename(columns={'Name': 'Full_Name', 'Age': 'Years'}, inplace=True)

df['City'] = df['City'].str.strip().str.upper()

print(df)