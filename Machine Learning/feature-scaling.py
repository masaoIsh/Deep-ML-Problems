import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	data = np.array(data, dtype=float)
	
	#Standardize
	data_transpose = data.T.copy()

	feature_means = [np.mean(row) for row in data_transpose]
	feature_stds = [np.sqrt(np.var(row)) for row in data_transpose]

	for i in range(len(data_transpose)):
		for j in range(len(data_transpose[0])):
			data_transpose[i][j] -= feature_means[i]
			data_transpose[i][j] /= feature_stds[i]
	
	standardized_data = data_transpose.T
	np.round(standardized_data, 4)

	#Min-max normalization
	data_transpose_two = data.T.copy()
	feature_maxes = [np.max(row) for row in data_transpose_two]
	feature_mins = [np.min(row) for row in data_transpose_two]

	for i in range(len(data_transpose_two)):
		for j in range(len(data_transpose_two[0])):
			data_transpose_two[i][j] -= feature_mins[i]
			data_transpose_two[i][j] /= (feature_maxes[i]-feature_mins[i])
	
	normalized_data = data_transpose_two.T
	np.round(normalized_data, 4)

	return standardized_data.tolist(), normalized_data.tolist()
