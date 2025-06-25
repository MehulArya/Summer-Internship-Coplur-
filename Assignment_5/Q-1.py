import pandas as pd

di = {"Author1" : "Takehiko Inoue", "Author2" : "Osho", "Authon3" : "Jane Austen"} # 1. Create a pandas Series from Dictionary
print(type(di))
print(pd.Series(di))

li = [0,1,2,3] # 2. Create a panda Series from the list
print(type(li))
print(pd.Series(li))

result = pd.Series(di) # Accessing the elements of a Series in panda
print(type(result))
print("Specific Index 0 : ", result[0])