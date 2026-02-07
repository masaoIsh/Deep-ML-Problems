import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	def sigmoid(x):
		return 1 / (1+np.exp(-1*x))
	
	weights = initial_weights
	bias = float(initial_bias)
	n = len(labels)

	mse_values = []

	for k in range(epochs):
		z = np.matmul(features, weights) + bias
		prediction = sigmoid(z)

		loss = round(sum([(labels[i]-prediction[i])**2 for i in range(n)]) / n, 4)
		mse_values.append(loss)

		error_term = 2*(prediction-labels)*sigmoid(z)*(1-sigmoid(z))

		gradient_w = (1/n) * np.matmul(features.T, error_term)
		#gradient_w = np.array([(1/n)*sum([2*(prediction[i]-labels[i])*(sigmoid(z[i])*(1 - sigmoid(z[i])))*features[i][j]] for i in range(n)) for j in range(len(features[0]))], dtype=float)
		gradient_b = np.mean(error_term)
		#gradient_b = (1/n)*sum([2*(prediction[i]-labels[i])*(sigmoid(z[i])*(1 - sigmoid(z[i])))] for i in range(n))
		
		weights = weights - learning_rate * gradient_w
		bias = bias - learning_rate * gradient_b
	
	weights = np.round(weights, 4)
	bias = round(bias, 4)
	return weights.tolist(), bias, mse_values
