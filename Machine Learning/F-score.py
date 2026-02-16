import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	n = y_true.shape[0]
	tp = 0
	fp = 0
	fn = 0
	tn = 0
	for i in range(n):
		if y_true[i] == 1:
			if y_pred[i] == 1:
				tp += 1
			else:
				fn += 1
		else:
			if y_pred[i] == 0:
				tn += 1
			else:
				fp += 1
	precision = (tp) / (tp + fp)
	recall = (tp) / (fn + tp)

	return round((1+beta**2)*((precision * recall) / ((beta**2 * precision)+recall)),  3)



