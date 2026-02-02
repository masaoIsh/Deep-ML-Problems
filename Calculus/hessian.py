from typing import Callable
import numpy as np

def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Hessian matrix of function f at the given point using finite differences.
	
	Args:
		f: A scalar function that takes a list of floats and returns a float
		point: The point at which to compute the Hessian (list of coordinates)
		h: Step size for finite differences (default: 1e-5)
		
	Returns:
		The Hessian matrix as a list of lists (n x n where n = len(point))
	"""
	# Your code here
	point = np.array(point, dtype=float)
	n = len(point)
	hessian = np.zeros((n, n))

	f_x = np.array(f(point), dtype=float)
	#print(f"f(point) is {f_x}")
	
	for i in range(n):
		for j in range(n):
			if i == j:
				point_new_plus = point.copy()
				point_new_minus = point.copy()
				point_new_plus[i] = point_new_plus[i]+h
				point_new_minus[i] = point_new_minus[i]-h

				f_x_new_plus = np.array(f(point_new_plus), dtype=float)
				f_x_new_minus = np.array(f(point_new_minus), dtype=float)

				hessian[i, j] = (f_x_new_plus - 2*f_x + f_x_new_minus) / (h**2)
			else:
				point_pp = point.copy()
				point_pm = point.copy()
				point_mp = point.copy()
				point_mm = point.copy()

				point_pp[i] += h
				point_pp[j] += h
				
				point_pm[i] += h
				point_pm[j] -= h

				point_mp[i] -= h
				point_mp[j] += h

				point_mm[i] -= h
				point_mm[j] -= h

				f_pp = np.array(f(point_pp), dtype=float)
				f_pm = np.array(f(point_pm), dtype=float)
				f_mp = np.array(f(point_mp), dtype=float)
				f_mm = np.array(f(point_mm), dtype=float)

				hessian[i, j] = (f_pp - f_pm - f_mp + f_mm) / (4*h*h)

	return hessian

