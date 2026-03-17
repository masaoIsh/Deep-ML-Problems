import math

def beta_distribution_stats(x: float, alpha: float, beta_param: float) -> dict:
    """
    Compute Beta distribution statistics.
    
    Args:
        x: Value at which to evaluate the PDF
        alpha: First shape parameter (alpha > 0)
        beta_param: Second shape parameter (beta > 0)
    
    Returns:
        Dictionary with 'pdf', 'mean', and 'variance'
    """
    # Your code here
        

    normalize = (math.gamma(alpha)*math.gamma(beta_param)) / math.gamma(alpha+beta_param) #B(alpha, beta)
    pdf = (1/normalize) * x**(alpha-1)*(1-x)**(beta_param-1) if (0 < x < 1) else 0.0
    
    val = {'pdf': pdf, 'mean': alpha / (alpha+beta_param), 'variance': (alpha*beta_param)/((alpha+beta_param)**2 * (alpha+beta_param+1))}

    return val
