import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr2 = np.array([1, 2, 3])

for x in arr:
  for y in x:
  	for z in y:
  		print(z)
for a in np.nditer(arr):
  print(a)
for idx, x in np.ndenumerate(arr):
  print(idx, x)
