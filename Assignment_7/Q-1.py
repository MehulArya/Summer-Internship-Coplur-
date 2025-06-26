import pandas as pd

# Sample data
data = pd.DataFrame(['$40,000*', '$40,000 conditions attached'], columns=['A'])

print("Original DataFrame:\n", data)

# Remove all non-digit characters using regex (\D+ matches any non-digit character)
data['A'] = data['A'].str.replace(r'\D+', '', regex=True).astype(int)

print("\nCleaned DataFrame (Only Numbers Extracted):\n", data)
