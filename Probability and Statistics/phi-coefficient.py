import numpy as np

def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	# Your code here
	contingency_table = np.zeros((2, 2))
	for i in range(len(x)):
		contingency_table[x[i]][y[i]] += 1
	
	a = contingency_table[0][0]
	b = contingency_table[0][1]
	c = contingency_table[1][0]
	d = contingency_table[1][1]

	numerator = a*d - b*c
	denominator = np.sqrt((a+b)*(c+d)*(a+c)*(b+d))
	val = numerator / denominator

	return round(val,4)
