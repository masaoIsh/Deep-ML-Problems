def exp_weighted_average(Q1, rewards, alpha):
    """
    Q1: float, initial estimate
    rewards: list or array of rewards, R_1 to R_k
    alpha: float, step size (0 < alpha <= 1)
    Returns: float, exponentially weighted average after k rewards
    """
    # Your code here
    total = 0
    k = len(rewards)
    for i in range(1, k+1):
        total += alpha * (1-alpha)**(k-i) * rewards[i-1]
    
    return ((1-alpha)**(k))*Q1 + total

