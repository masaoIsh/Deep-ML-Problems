import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g_coeffs = np.array(g_coeffs).astype(float)
    h_coeffs = np.array(h_coeffs).astype(float)

    if len(g_coeffs) <= 1:
        g_prime_coeffs = np.array([0.0])
    else:
        g_prime_coeffs = g_coeffs[:-1] * range(len(g_coeffs)-1, 0, -1)
    
    if len(h_coeffs) < 1:
        h_prime_coeffs = np.array([0.0])
    else:
        h_prime_coeffs = h_coeffs[:-1] * range(len(h_coeffs)-1, 0, -1)

    #numerator
    first_term = np.polymul(g_prime_coeffs, h_coeffs)
    second_term = np.polymul(g_coeffs, h_prime_coeffs)
    numerator = np.polysub(first_term, second_term)
    #numerator_reverse = np.flip(numerator)
    #numerator_x = sum([numerator_reverse[i-1]*(x**(i-1)) for i in range(len(numerator_reverse), 0, -1)])
    numerator_x = np.polyval(numerator, x)

    #denominator
    denominator = np.polymul(h_coeffs, h_coeffs)
    #denominator_reverse = np.flip(denominator)
    #denominator_x = sum([denominator_reverse[i-1]*(x**(i-1)) for i in range(len(denominator_reverse), 0, -1)])
    denominator_x = np.polyval(denominator, x)
    
    return numerator_x / denominator_x






