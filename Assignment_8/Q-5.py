import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Created array and its data type: \n", arr, arr.dtype)
float_arr = arr.astype(float) # Convert the array to float type
print("Converted array and its data type: \n", float_arr, float_arr.dtype)