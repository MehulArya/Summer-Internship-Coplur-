import numpy as np
arr1 = np.arange(2,9) # array with a range 2 to 9
arr2 = np.arange(2,9) # array with a range 2 to 9
arr3 = np.arange(2,9) # array with a range 2 to 9

res_arr = np.stack([arr1,arr2,arr3])
print("3X3 Matrix with values ranging from 2 to 10: \n", res_arr)