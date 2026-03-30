import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp = sum([int(y_true[i]==1 and y_pred[i]==1) for i in range(len(y_true))])
	fp = sum([int(y_true[i]==0 and y_pred[i]==1) for i in range(len(y_true))])

	return tp / (tp + fp)

