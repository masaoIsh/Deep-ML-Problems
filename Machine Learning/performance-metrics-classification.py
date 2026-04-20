
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	tp = sum([int(actual[i]==1 and predicted[i]==1) for i in range(len(actual))])
	fp = sum([int(actual[i]==0 and predicted[i]==1) for i in range(len(actual))])
	fn = sum([int(actual[i]==1 and predicted[i]==0) for i in range(len(actual))])
	tn = sum([int(actual[i]==0 and predicted[i]==0) for i in range(len(actual))])

	confusion_matrix = [[tp, fn], [fp, tn]]
	accuracy = (tp+tn) / (tp+fp+fn+tn)
	precision = (tp) / (tp+fp)
	negativePredictive = (tn) / (tn+fn)
	specificity = (tn) / (tn+fp)
	recall = (tp) / (tp+fn)

	f1 = 2 * (precision*recall) / (precision+recall)

	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)

