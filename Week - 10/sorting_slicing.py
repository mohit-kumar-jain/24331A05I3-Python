import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [23, 45, 12, 36, 29],
    'Marks': [88, 92, 79, 85, 90]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by='Age')
sorted_desc = df.sort_values(by='Marks', ascending=False)

slice_rows = df[0:3]
slice_cols = df[['Name', 'Marks']]
loc_slice = df.loc[0:2, ['Name', 'Age']]
iloc_slice = df.iloc[0:3, 0:2]

print(df)
print(sorted_df)
print(sorted_desc)
print(slice_rows)
print(slice_cols)
print(loc_slice)
print(iloc_slice)