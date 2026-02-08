import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	if seed != None:
		np.random.seed(seed)

	row_indices = np.arange(X.shape[0])
	np.random.shuffle(row_indices)
	return (X[row_indices], y[row_indices])
