import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr2 = np.array([1, 2, 3, 4], ndmin=5)
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr3.reshape(2, 3, 2)

print(arr.shape)
print(arr2)
print('shape of array :', arr2.shape)
print(newarr)
