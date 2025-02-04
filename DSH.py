import numpy as np

# 1. Create an array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# 2. Array shape
print("Shape of the array:", arr.shape)

# 3. Reshaping the array
reshaped_arr = arr.reshape(1, 5)
print("Reshaped array:", reshaped_arr)

# 4. Element-wise addition and multiplication
added_arr = arr + 2
multiplied_arr = arr * 3
print("Array after addition (arr + 2):", added_arr)
print("Array after multiplication (arr * 3):", multiplied_arr)

# 5. Sum and Mean of the array
total = arr.sum()
mean_val = arr.mean()
print("Sum of the array:", total)
print("Mean of the array:", mean_val)

# 6. Indexing and slicing
element = arr[2]
sliced_arr = arr[1:4]
print("Element at index 2:", element)
print("Sliced array:", sliced_arr)