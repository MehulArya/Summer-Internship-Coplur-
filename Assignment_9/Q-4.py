import numpy as np
arr = np.array([[0,1,2,3,4,5],[10,11,6,7,8,9]])
print("Original Array: \n", arr)
max_el = arr.max()
print("Maximum Value of Array: ", max_el) # 1. Maximum Element

min_el = arr.min()
print("Minimum Value of Array: ", min_el) # 2. Minimum Element

rows, col = arr.shape # 3. Find rows and columns of a given array
print("Rows in the Array are: ", rows)
print("Column in the Array are: ", col)

x = int(input(f"What Element to Find in Original Array: ")) # 3. Find a Specefic Element in the given array
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == x:
            print("Row:", i, "Col:", j)

sum = 0 # 4. Sum of all the values in a 2-D Array using for loop
for i in np.nditer(arr):
        sum += i
print("Sum of all the Values in a 2-D Array: \n", sum)

a = np.array([1,2,3]) # 5. Adding, Multiplying, difference and sum on array
b = np.array([4,5,6])
print("Array a: \n",a)
print("Array b: \n", b)
c = a + b
print("Sum of a and b: \n",c)
c = a * b
print("Product of a and b: \n",c)
c = a - b
print("Subtraction of a and b: \n",c)
c = a / b
print("Division of a and b: \n",c)