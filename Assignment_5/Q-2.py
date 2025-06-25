import pandas as pd
# 1. Make Pandas DataFrame with a python Two-Dimensional Python list
li = [["Captain America","Vibranium Shield","Defence"], ["Iron Man","Arc Reactor", "Power-Supply"]]
print(type(li))
df = pd.DataFrame(li)
print(df)

# 2. Create Dataframe from Python dict
dict = {"fruit":["Apple", "Orange", "Berry"], "Price":[90, 75, 100]}
print(type(dict))
df = pd.DataFrame(dict)
print(df)

# 3. Create Pandas DataFrame using List of Lists
li1 = [["Captain America","Vibranium Shield","Defence"], ["Iron Man","Arc Reactor", "Power-Supply"]]
print(type(li))
df = pd.DataFrame(li1)
print(df)

# 4. Create a Pandas DataFrame from list of tuples
li_of_tu = [("Captain America","Vibranium Shield","Defence"), ("Iron Man","Arc Reactor", "Power-Supply")]
print(type(li_of_tu))
df = pd.DataFrame(li_of_tu)
print(df)

# 5. Create a Pandas DataFrame From List of Dicts
li_of_dict = [{"summerFruit":["WaterMelon", "Mango", "Lychee"], "Price":[90, 75, 100]}, {"winterFruit":["Peach", "Raspberry", "Black berry"], "Price":[100, 85, 60]}]
print(type(li_of_dict))
df = pd.DataFrame(li_of_dict)
print(df)