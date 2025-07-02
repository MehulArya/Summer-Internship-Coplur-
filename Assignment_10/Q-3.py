import numpy as np

arr = np.array([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]])
print(arr)
col_mean = np.nanmean(arr, axis=0) # ignore nan
arr = np.nan_to_num(arr, nan=col_mean)
print("Array after replacing NaN with column averages:\n", arr)
