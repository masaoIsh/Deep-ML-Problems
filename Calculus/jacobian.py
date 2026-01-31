import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	# Your code here
	x = np.array(x, dtype=float)
	n = len(x)

	f_x = np.array(f(x), dtype=float)
	#print(f"The function output is {f_x}")
	m = len(f_x)

	jacobian = np.zeros((m, n))
	
	for i in range(n):
		x_new = x.copy() #copy of input array (ie the point)
		x_new[i] = x_new[i] + h #add h for deriv computation

		f_plus_h = np.array(f(x_new), dtype=float)

		jacobian[:, i] = (f_plus_h-f_x) / h
		#print(f"Foo[i] is {foo[i]}")

	
	return jacobian



	
