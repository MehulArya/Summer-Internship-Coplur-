import numpy as np

arr = np.array([[6, -8, 73, -110],[np.nan, -8, 0, 94]])

# Replace NaN with 0
arr = np.nan_to_num(arr, nan=0)
print("Nan Values changed to 0: \n", arr)

arr = arr[:, :3]

new_row = np.array([[0, 0, 0]]) # cause there are no 3 rows only 2
arr = np.vstack([arr, new_row])

#Interchange rows 0 and 2, columns 0 and 2
arr[[0, 2]] = arr[[2, 0]]
arr[:, [0, 2]] = arr[:, [2, 0]]
print("Row and Column changed: \n", arr)
arr[[0,1]] = arr[[1,0]]
arr[:, [0,1]] = arr[:, [1,0]]
print("Row and Column changed: \n", arr)
arr[[1,2]] = arr[[2,1]]
arr[:, [2,1]] = arr[:,[1,2]]
print("Row and Column changed: \n", arr)

