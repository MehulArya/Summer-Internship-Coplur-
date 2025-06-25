import pandas as pd
a = {'Fruits':["Apple", "Orange", "Mango", "Kiwi"],'Pricing':[90,80,100,70], 'Freshness':[True, False, True, False]}
df = pd.DataFrame(a)
print(df)
result = df[df['Pricing'] == 90] # 1. Selecting rows in panda DataFrame based on Location
print(result)

result = df.iloc[1:2, :] # 2. Select Any row from a DataFrame using iloc
print(result)

result = df.loc[0:2, 'Fruits':'Pricing'] # 3. Limited Row Selection with given column
print(result)

result = df.drop(df[df['Pricing'] == 90]) # 4. Drop Row from the Data Frame based on certain condition applied in a column
print(result)

result = (df.iloc[0:, :]).tolist() # 5. Create a List from rows in Pandas DataFrame
print(result)