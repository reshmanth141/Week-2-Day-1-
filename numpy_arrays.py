import numpy as np

# Create a one-dimensional array
array_1d = np.array([10, 20, 30, 40, 50])

# Create a two-dimensional array
array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("1D Array:")
print(array_1d)
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Number of dimensions:", array_1d.ndim)

print("\n2D Array:")
print(array_2d)
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Number of dimensions:", array_2d.ndim)