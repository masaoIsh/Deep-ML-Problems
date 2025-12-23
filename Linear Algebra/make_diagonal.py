import numpy as np

def make_diagonal(x):
	# Your code here
    # use np.array()
    x = np.array(x)
    a = np.zeros((len(x), len(x)))
    for i in range(a.shape[0]):
        a[i][i] = x[i]
    return a
