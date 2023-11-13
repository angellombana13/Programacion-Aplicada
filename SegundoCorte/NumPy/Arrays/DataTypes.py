import numpy as np

arr1 = np.array([1, 2, 3, 4], dtype='S')
arr2 = np.array(['apple', 'banana', 'cherry'])
arr3 = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(arr1.dtype)
print(arr2.dtype)
print(newarr)
print(newarr.dtype)
