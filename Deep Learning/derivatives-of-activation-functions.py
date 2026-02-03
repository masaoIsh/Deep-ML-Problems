import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	if x <= 0:
		relu = 0.0
	else:
		relu = 1.0

	sigma = lambda x: 1 / (1+np.exp(-x))
	sigmoid = sigma(x)*(1-sigma(x))

	hyperbolic_tangent = lambda x: (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
	tanh = 1 - hyperbolic_tangent(x) ** 2
	
	derivatives = {
		'sigmoid': sigmoid,
		'tanh': tanh,
		'relu': relu
	}

	return derivatives


