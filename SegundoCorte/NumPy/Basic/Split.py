import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)
newarr2 = np.array_split(arr, 6)

print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr2)
