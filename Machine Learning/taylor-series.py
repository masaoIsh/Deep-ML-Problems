import numpy as np
from math import factorial

def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    """
    Compute Taylor series approximation for common functions.
    
    Args:
        func_name: Name of function ('exp', 'sin', 'cos')
        x: Point at which to evaluate
        n_terms: Number of terms in the series
    
    Returns:
        Taylor series approximation rounded to 6 decimal places
    """
    if func_name == 'exp':
        approx = 0
        def f(n):
            return x**n / (factorial(n))
        for i in range(n_terms):
            approx += f(i)
        return round(approx, 6)
    elif func_name == 'sin':
        approx = 0
        def f(n):
            return ((-1)**n / factorial(2*n+1)) * x**(2*n+1)
        for i in range(n_terms):
            approx += f(i)
        return round(approx, 6)
    elif func_name == 'cos':
        approx = 0
        def f(n):
            return ((-1)**n / factorial(2*n)) * x**(2*n)
        for i in range(n_terms):
            approx += f(i)
        return round(approx, 6)
    else:
        raise ValueError("Please enter a valid function name.")
