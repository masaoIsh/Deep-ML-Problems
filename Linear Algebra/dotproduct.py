import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	"""
	dot_product = 0
    if (len(vec1) != len(vec2)):
        return -1

    for i in range(len(vec1)):
        dot_product += vec1[i]*vec2[i]
    return dot_product

