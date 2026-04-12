import numpy as np

def binary_cross_entropy(y_true: list[float], y_pred: list[float], epsilon: float = 1e-15) -> float:
	"""
	Compute binary cross-entropy loss.
	
	Args:
		y_true: True binary labels (0 or 1)
		y_pred: Predicted probabilities (between 0 and 1)
		epsilon: Small value for numerical stability
	
	Returns:
		Mean binary cross-entropy loss
	"""
	# Your code here
	return -1*np.mean([y_true[i]*np.log(y_pred[i]) + (1-y_true[i])*np.log(1-y_pred[i]) for i in range(len(y_true))])
