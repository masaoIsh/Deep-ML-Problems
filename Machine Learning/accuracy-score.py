import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	num_correct = 0
	for i in range(len(y_true)):
		if y_true[i] == y_pred[i]:
			num_correct += 1
	
	return num_correct / len(y_pred)
