import numpy as np

arr1 = np.arange(3)
arr2 = np.arange(4,7)
arr3 = np.arange(7,10)
array3D = np.vstack([arr1, arr2, arr3]).reshape(3,3)
print("3-D Array: \n", array3D)
# Move axis 0 to 2nd position
moved = array3D.T
print("Original shape: \n", array3D)
print("Moved axes shape: \n", moved)
