import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	# Your code here
	def softmax(a):
		exp_x = [np.exp(x[i]) for i in range(len(x))]
		sum_exp = sum(exp_x)
		return np.exp(x[a]) / sum_exp

	jacobian = [[0 for i in range(len(x))] for j in range(len(x))]
	
	for i in range(len(jacobian)):
		for j in range(len(jacobian[0])):
			if i == j:
				jacobian[i][j] = softmax(i) * (1-softmax(i))
			else:
				jacobian[i][j] = softmax(i)*softmax(j)*-1


	return jacobian
