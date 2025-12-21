import numpy as np

arr = np.array([[10,20,30],[40,50,60]])
print("Original 2D array : ")
print(arr)
print("Shape of array : ",arr.shape)
print("Size of array : ",arr.size)
print("Total Sum : ",np.sum(arr))
print("Row-wise Sum : ",np.sum(arr,axis=1))
print("Column-wise Sum : ",np.sum(arr,axis=0))
print("Transpose of Array is : ",arr.T)