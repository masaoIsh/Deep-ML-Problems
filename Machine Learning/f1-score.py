def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	# Your code here
	n = len(y_true)
	
	tp = 0
	fn = 0
	fp = 0
	for i in range(n):
		if y_true[i] == 1 and y_pred[i] == 1:
			tp += 1
		if y_true[i] == 1 and y_pred[i] == 0:
			fn += 1
		if y_true[i] == 0 and y_pred[i] == 1:
			fp += 1

	precision = tp / (tp + fp) if (tp + fp) != 0 else 0.0
	recall = tp / (tp + fn) if (tp + fn) != 0 else 0.0
	if precision + recall == 0:
		return 0.0
	f1 = 2 * (precision * recall) / (precision + recall)
	
	return round(f1,3)
