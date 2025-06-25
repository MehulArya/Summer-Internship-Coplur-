import pandas as pd

df1 = pd.DataFrame({"id":[1,2,3,4],"Name": ["a1", "a2", "a3", "a4"], "Subject":["sub","sub2","sub3","sub4"]}, index=[1,2,3,4])
df2 = pd.DataFrame({"id":[1,2,3], "Name": ["b1", "b2", "b3"], "Subject":["sub1","sub2","sub3"]}, index=[1,2,3])

result = df1.merge(df2, on='id', how='inner') # 1 . Perform Inner Merge
print(result)

# Output:
# id Name_x Subject_x Name_y Subject_y
# 0   1     a1       sub     b1      sub1
# 1   2     a2      sub2     b2      sub2
# 2   3     a3      sub3     b3      sub3

result = df1.merge(df2, on="id", how="left") # 2. Perform a Left Join of df1 and df2
print(result)

# Output:
#    id Name_x Subject_x Name_y Subject_y
# 0   1     a1       sub     b1      sub1
# 1   2     a2      sub2     b2      sub2
# 2   3     a3      sub3     b3      sub3
# 3   4     a4      sub4    NaN       NaN

# Missing values from df2 on id 4 are returning NaN as we do left join so it takes id of df1 in consideration to merge

result = df1.merge(df2, on="id", how="right") # 3. Perform a  Right Join of df1 and df2
print(result)

# Output:
#    id Name_x Subject_x Name_y Subject_y
# 0   1     a1       sub     b1      sub1
# 1   2     a2      sub2     b2      sub2
# 2   3     a3      sub3     b3      sub3

# Missing Values of id 4 in df1 as this time we take the id of df2 in consideration as it is right merge and only prints id upto 3

result = df1.join(df2, lsuffix="-left", rsuffix="-right") # 4. Perform a index-based join
print(result)

# Output:
#    id-left Name-left Subject-left  id-right Name-right Subject-right
# 1        1        a1          sub       1.0         b1          sub1
# 2        2        a2         sub2       2.0         b2          sub2
# 3        3        a3         sub3       3.0         b3          sub3
# 4        4        a4         sub4       NaN        NaN           NaN

result = df1.merge(df2, on="id", how="right") # 5. Perform a Right Merge and join then compare their output
print(result)
# Output1:
#    id Name_x Subject_x Name_y Subject_y
# 0   1     a1       sub     b1      sub1
# 1   2     a2      sub2     b2      sub2
# 2   3     a3      sub3     b3      sub3

result = df1.join(df2, lsuffix="-left", rsuffix="-right")
print(result)

# Output2:
#    id-left Name-left Subject-left  id-right Name-right Subject-right
# 1        1        a1          sub       1.0         b1          sub1
# 2        2        a2         sub2       2.0         b2          sub2
# 3        3        a3         sub3       3.0         b3          sub3
# 4        4        a4         sub4       NaN        NaN           NaN

# Comparing Output1 and Output2, we can conclude that on doing a right merge we only get the values
# of the right dataframe(or any object which is being used of Pandas) whereas join allows us to see
# all the values it does not depend on any one dataframe for index like in right or left merge.

result = df1.merge(df2, on=['id','Subject']) # 6. Performing merge on multiple keys
print(result)