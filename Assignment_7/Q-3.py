import pandas as pd
data = pd.read_csv('fake.csv')
print(data)

df = pd.DataFrame(data)
print(data)

print(df.head(10)) # top 10 rows
print(df.tail(10)) # last 10 values
print(df.info()) # Gives information about Data

print(df.describe())

print(df.shape) # Describes  the shape of data

print(df['c1'])

filter_df = df[df['c1'] > 0] # Gives The values more than 0
print(filter_df.head()) # Shows top 5 values from the top

group_data = df.groupby('degree')['salary'].mean()
print(group_data.head())

print(df['degree'].value_counts()) # Counts the number of a specific Degree

pd.options.display.max_rows = 500
df = pd.read_csv('fake.csv')
print(df)

# drop empty rows / Data Cleaning
df = df.dropna()
print(df)

df = df.fillna(5)
print(df)

df = df.ffill()
print(df)