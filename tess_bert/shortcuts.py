import numpy as np

# https://stackoverflow.com/questions/49330080/numpy-2d-array-selecting-indices-in-a-circle
def circular_mask(arr_shape, cx, cy, r):
    y = np.arange(arr_shape[0])
    x = np.arange(arr_shape[1])
    return ((x[np.newaxis, :] - cx) ** 2 + (y[:, np.newaxis] - cy) ** 2) < (r ** 2)  # noqa
