def law_of_total_probability(priors: dict, conditionals: dict) -> float:
    """
    Compute P(A) using the Law of Total Probability.
    
    Args:
        priors: Dictionary mapping partition event names to P(Bi)
        conditionals: Dictionary mapping partition event names to P(A|Bi)
    
    Returns:
        float: The total probability P(A), rounded to 4 decimal places
    """
    # Your code here
    p_a = 0.0
    for key in priors:
        p_a += priors[key]*conditionals[key]

    return p_a
