import numpy as np

arr = np.array([5, 15, 25, 35, 45])
result = np.clip(arr, 10, 30)

print(result)