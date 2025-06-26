import pandas as pd

data = {
    'date': ['2025-06-26', '2025-06-30', '2025-06-15', '2025-06-11']
}

df = pd.DataFrame(data)
print(df)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])
print(df)

# Extract year, month, day
df['year'] = df['date'].dt.year
print(df)
df['month'] = df['date'].dt.month
print(df)
df['day'] = df['date'].dt.day
print(df)

# Weekday name and number
df['weekday_name'] = df['date'].dt.day_name()
print(df)
df['weekday_num'] = df['date'].dt.weekday  # Monday = 0
print(df)

# Week of the year
df['week_number'] = df['date'].dt.isocalendar().week
print(df)

# Start and end of month/year
df['is_month_start'] = df['date'].dt.is_month_start
print(df)
df['is_month_end'] = df['date'].dt.is_month_end
print(df)
df['is_year_start'] = df['date'].dt.is_year_start
print(df)
df['is_year_end'] = df['date'].dt.is_year_end
print(df)

# Filtered Date
filtered = df[(df['date'] >= '2025-06-20') & (df['date'] <= '2025-06-30')]
print(filtered)