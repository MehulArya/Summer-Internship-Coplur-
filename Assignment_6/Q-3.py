import pandas as pd
a = pd.DataFrame({'Table1':[1,2,3],'Table2': [4,5,6]})
b = pd.DataFrame({'Table1':[7,8,9],'Table2': [10,11,12]})
c = pd.DataFrame({'Table1':[5,6,7],'Table2': [10,11,12]})

result = pd.concat([a,b], keys=['a','b','c'], axis=1) # 1. Concatenate two data frame vertically
print(result)

# Output:
#        a             b
#   Table1 Table2 Table1 Table2
# 0      1      4      7     10
# 1      2      5      8     11
# 2      3      6      9     12

result1 = c.merge(result['b'], on="Table2") # 2. Merge the result of previous operation with the third Data Frame
print(result1)

# Output:
#    Table1_x  Table2  Table1_y
# 0         5      10         7
# 1         6      11         8
# 2         7      12         9

# 3. The Primary Difference between df.join() and pd.merge is as follows:
#    df.join() -> works as index-based join whereas pd.merge() -> works as SQL like join/merge.