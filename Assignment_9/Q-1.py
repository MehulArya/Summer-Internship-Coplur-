import numpy as np
arr1 = np.array([1,2,3,4])
print("1-D Array: \n", arr1)
arr2 = np.array([[5,6,7,8],[9,10,11,12]])
print("2-D Array: \n", arr2)
arr1_reshaped = arr1.reshape(1, 4)
concatenate_array = np.concatenate((arr1_reshaped,arr2))
print("Concatenate Array: \n", concatenate_array)