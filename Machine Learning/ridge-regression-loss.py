import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
    regularization = alpha*np.sum([weight**2 for weight in w])
	loss = np.mean([(y_true - np.matmul(X, w))**2])
    
    return loss + regularization

