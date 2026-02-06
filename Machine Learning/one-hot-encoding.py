import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col == None:
		n_col = max(x)+1

	output = np.array([np.zeros(n_col) for i in range(len(x))])
	for i in range(len(output)):
		for j in range(len(output[0])):
			if j == x[i]:
				output[i][j] = 1

	return output
