import math

def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
	# Your code here
	def sigmoid(a):
		return 1 / (1+math.exp(-1*a))
	
	return x * sigmoid(x)
