import numpy as np

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	# Your code here
	def softmax(index):
		denominator = sum([np.exp(logit) for logit in logits])
		numerator = np.exp(logits[index])
		return numerator / denominator

	distribution = [softmax(i) for i in range(len(logits))]
	one_hot = [0 for i in range(len(logits))]
	for i in range(len(one_hot)):
		if i == target:
			one_hot[i] = 1

	return [distribution[k] - one_hot[k] for k in range(len(one_hot))]
