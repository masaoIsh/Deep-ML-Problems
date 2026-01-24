import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    f_coeffs = np.array(f_coeffs).astype(float)
    g_coeffs = np.array(g_coeffs).astype(float)

    if len(f_coeffs) <= 1:
        f_prime_coeffs = np.array([0.0])
    else:
        f_prime_coeffs = f_coeffs[1:] * np.arange(1, len(f_coeffs))
    
    if len(g_coeffs) <= 1:
        g_prime_coeffs = np.array([0.0])
    else:
        g_prime_coeffs = g_coeffs[1:] * np.arange(1, len(g_coeffs))
    
    first_term = np.convolve(f_prime_coeffs, g_coeffs)
    second_term = np.convolve(g_prime_coeffs, f_coeffs)

    longer_length = max(len(first_term), len(second_term)) 
    if len(first_term) != longer_length: 
        first_term = np.pad(first_term, (0, longer_length - len(first_term))) 
    if len(second_term) != longer_length: 
        second_term = np.pad(second_term, (0, longer_length - len(second_term))) 
    result = first_term + second_term 
    nonzero = np.nonzero(result)[0]
    if len(nonzero) == 0:
        return [0.0]
    last = np.nonzero(result)[0][-1] 
    result = result[:last+1] 
    
    return result.tolist()




