import pandas as pd

dates = ['25-06-2025', '26-06-2025', '27-06-2025']
values = [100, 200, 300]

indexDate = pd.to_datetime(dates, format='%d-%m-%Y')
print(indexDate)

result = pd.Series(data=values, index=indexDate)
print(result)

# Output:
# 2025-06-25    100
# 2025-06-26    200
# 2025-06-27    300