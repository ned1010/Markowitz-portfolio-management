import numpy as np

# create a sample numpy array
arr = np.array([10, 20, 30, 40, 50])

# calculate the difference between consecutive values
diff = np.diff(arr)

# shift the array down by one element
shifted_arr = np.roll(arr, -1)

# divide the difference by the second value
result = diff/shifted_arr[:-1]
print(result)
