import numpy as np
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
print("Array A: \n", A)
B = np.array([9, -6, 17])
print("Array B: \n", B)

# using linalg.inv
A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)
print("Solution using inverse matrix:", X)

# using linalg.solve
X2 = np.linalg.solve(A, B)
print("Solution using linalg.solve:", X2)
