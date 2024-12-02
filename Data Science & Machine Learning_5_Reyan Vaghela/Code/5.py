import numpy as np

def moving_average(arr, window_size):

    if window_size <= 0:
        raise ValueError("Window size must be a positive integer.")
    if window_size > len(arr):
        raise ValueError("Window size must not be greater than the length of the array.")


    moving_avg = []
    for i in range(len(arr) - window_size + 1):
        avg = np.mean(arr[i:i + window_size])
        moving_avg.append(avg)

    return np.array(moving_avg)

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
window_size = 2
result = moving_average(data, window_size)
print(result)