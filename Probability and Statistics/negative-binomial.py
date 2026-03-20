import math

def negative_binomial_pmf(k: int, r: int, p: float) -> float:
    """
    Calculate the probability of observing exactly k failures
    before achieving r successes in independent Bernoulli trials.
    
    Args:
        k: Number of failures (non-negative integer)
        r: Number of successes required (positive integer)
        p: Probability of success on each trial (0 < p <= 1)
    
    Returns:
        Probability P(X = k) rounded to 5 decimal places
    """
    # Your code here
    # 最初のk+r-1でrー1回成功する方法の総数
    binom = math.comb(k+r-1, r-1)
    # rー1回成功する確率 x p
    sucesses = p**(r-1) * p
    # k回失敗する確率
    failures = (1-p)**k

    val = binom * sucesses * failures

    return round(val, 5)
