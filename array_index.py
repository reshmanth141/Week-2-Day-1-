import numpy as np


array = np.array(
	[
		[10, 20, 30, 40],
		[50, 60, 70, 80],
		[90, 100, 110, 120],
	]
)

print("First element:", array[0, 0])
print("Last element:", array[-1, -1])

# Complete rows and columns
print("First row:", array[0, :])
print("Last row:", array[-1, :])
print("First column:", array[:, 0])
print("Last column:", array[:, -1])

print("Top-left 2x2 section:\n", array[:2, :2])
print("Rows 1-2, columns 2-4:\n", array[1:, 1:])
print("Every other column:\n", array[:, ::2])
print("Rows in reverse order:\n", array[::-1, :])
