import numpy as np

arr1 = np.array([[3, 4], [1, 2]])
arr2 = np.array([[5, 6], [7, 8]])

avg = (arr1 + arr2) / 2
print("Element-wise Average:\n", avg)

combined_flatten = np.concatenate((arr1.flatten(), arr2.flatten()))

# Mean
mean_val = np.mean(combined_flatten)

# Median
median_val = np.median(combined_flatten)

# Mode
unique, counts = np.unique(combined_flatten, return_counts=True)
mode_val = unique[np.argmax(counts)]

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)
