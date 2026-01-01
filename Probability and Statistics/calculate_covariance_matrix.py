def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    num_features = len(vectors)
    num_datapoints = len(vectors[0])
    
    means = [(sum(vectors[i]) / len(vectors[i])) for i in range(len(vectors))]
    cov_matrix = [[0 for _ in range(len(vectors))] for _ in range(len(vectors))]

    for i in range(num_features):
        for j in range(i, num_features):
            cov_matrix[i][j] = sum([(vectors[i][k]-means[i])*(vectors[j][k]-means[j]) for k in range(num_datapoints)]) / (num_datapoints-1)
            cov_matrix[j][i] = cov_matrix[i][j]
    
    return cov_matrix
