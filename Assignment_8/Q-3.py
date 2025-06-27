import numpy as np

null_vector = np.zeros(10) # Null-Vector of size 10
print("Null Vector before updating data: \n", null_vector)
null_vector[5] = 11
print("Vector after updating data: \n", null_vector)
