import numpy as np


def array_math_operations(array1, array2):
	"""Return element-wise addition, subtraction, multiplication, and division."""
	array1 = np.asarray(array1)
	array2 = np.asarray(array2)

	if array1.shape != array2.shape:
		raise ValueError("Arrays must have the same shape.")
	if np.any(array2 == 0):
		raise ZeroDivisionError("Cannot divide by zero.")

	return (
		array1 + array2,
		array1 - array2,
		array1 * array2,
		array1 / array2,
	)


if __name__ == "__main__":
	first = np.array([10, 20, 30])
	second = np.array([2, 4, 5])

	addition, subtraction, multiplication, division = array_math_operations(
		first, second
	)
	print("Addition:", addition)
	print("Subtraction:", subtraction)
	print("Multiplication:", multiplication)
	print("Division:", division)
