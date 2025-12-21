import numpy as np

arr = np.array([151,110,45,120,251])
print("Array :",arr)
print("First element :",arr[0])
print("Elemnts from Index 1 to 3 :",arr[1:4])
print("Last element :",arr[-1])

print("Size of array :",np.size(arr))
print("Sorted array is:",np.sort(arr))
print("Index of Maximum value in array is:",np.argmax(arr))
print("Index of Minimum value in array is:",np.argmin(arr))
print("Cumulative Sum : ",np.cumsum(arr))