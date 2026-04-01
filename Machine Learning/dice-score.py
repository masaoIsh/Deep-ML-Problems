
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	tp = sum([int(y_true[i]==1 and y_pred[i]==1) for i in range(len(y_true))])
	fp = sum([int(y_true[i]==0 and y_pred[i]==1) for i in range(len(y_true))])
	fn = sum([int(y_true[i]==1 and y_pred[i]==0) for i in range(len(y_true))])
	res = (2*tp) / (2*tp + fp + fn) if (2*tp + fp + fn) != 0 else 0.0

	return round(res, 3)

