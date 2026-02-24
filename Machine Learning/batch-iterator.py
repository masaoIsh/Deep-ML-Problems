import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	sample_size = X.shape[0]
	output = []
	for i in np.arange(0, sample_size, batch_size):
		batch = []
		start, end = i, min(i + batch_size, sample_size)
		batch.append(X[start:end].tolist())
		if y is not None:
			batch.append(y[start:end].tolist())
		output.append(batch)
	
	return output
