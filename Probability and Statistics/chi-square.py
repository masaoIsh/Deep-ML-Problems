import math

def chi_square_probability(x, k):
    """
    Calculate the probability density of x in a Chi-square distribution
    with k degrees of freedom.
    """
    # your code here
    probability = 1/(2**(k/2)*math.gamma(k/2)) * x**((k/2)-1) * math.exp(-1*(x/2))
    return round(probability, 3)
