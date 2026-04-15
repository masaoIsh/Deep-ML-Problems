import numpy as np

def gaussian_mle(data: np.ndarray) -> tuple:
    """
    Compute Maximum Likelihood Estimates for Gaussian distribution parameters.
    
    Args:
        data: 1D numpy array of observations
        
    Returns:
        Tuple of (mean_mle, variance_mle)
    """
    # Your code here
    mean_mle = np.mean(data)
    variance_mle = (1/len(data)) * sum([(data[i]-mean_mle)**2 for i in range(len(data))])

    return (mean_mle, variance_mle)
