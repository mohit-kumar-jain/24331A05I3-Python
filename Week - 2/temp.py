import numpy as np

# Creating a 2D NumPy array
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Original 2D Array:",arr)
# print(arr)

# Shape and size
print("Shape of array:", arr.shape)
print("Size of array:", arr.size)

# Sum operations
print("Total Sum:", np.sum(arr))
print("Row-wise Sum:", np.sum(arr, axis=1))
print("Column-wise Sum:", np.sum(arr, axis=0))

# Statistical functions
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Mean value:", np.mean(arr))

# Transpose
print("Transpose of array:")
print(arr.T)
