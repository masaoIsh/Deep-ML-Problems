import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # Your code here
    sample_size = X.shape[0]
    #weights = weights.copy()
    if method == 'batch':
        for i in range(n_epochs):
            #grad = np.zeros_like(weights)
            #for j in range(sample_size):
            pred = X @ weights
            error = pred - y
            grad = (2/sample_size) * X.T @ error
            weights = weights - learning_rate * grad
        return weights
    elif method == 'stochastic':
        for i in range(n_epochs):
            for j in range(sample_size):
                pred = X[j] @ weights
                error = pred - y[j]
                grad = 2 * (X[j].T * error)
                weights = weights - learning_rate * grad
        return weights
    elif method == 'mini_batch':
        for i in range(n_epochs):
            for j in np.arange(0, sample_size, batch_size):
                start, end = j, min(j+batch_size, sample_size)
                pred = X[start:end] @ weights
                error = pred - y[start:end]
                grad = (2/(end-start)) * (X[start:end].T @ error)
                weights -= learning_rate * grad
        return weights
    else:
        raise ValueError("invalid method")

