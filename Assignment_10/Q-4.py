import numpy as np

arr = np.array([1, -3, 5, -7, 9])
print("Original Array: \n", arr)
# Replace negatives with zero
arr[arr < 0] = 0
print("Replaced negative values with 0:\n", arr)
