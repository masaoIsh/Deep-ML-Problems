import numpy as np

def exponential_distribution(x: list, lam: float) -> dict:
    """
    Compute exponential distribution properties.
    
    Args:
        x: Points at which to evaluate PDF and CDF
        lam: Rate parameter (lambda) of the distribution
        
    Returns:
        Dictionary with 'pdf', 'cdf', 'mean', and 'variance' keys
    """
    # Your code here
    # f(x) = \lambda * exp(-\lambda x)
    if lam <= 0:
        return {'pdf': None, 'cdf': None, 'mean': None, 'variance': None}
    
    pdf = [round(lam * np.exp(-1 * lam * x[i]), 4) if x[i] >= 0 else 0.0 for i in range(len(x))]
    
    cdf = [round(1-np.exp(-1*lam*x[i]), 4) if x[i] >= 0 else 0.0 for i in range(len(x))]
    
    mean = round(1/lam, 4)
    variance = round(1/(lam**2), 4)

    return {'pdf': pdf, 'cdf': cdf, 'mean': mean, 'variance': variance}
    

