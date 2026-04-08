import numpy as np

def create_bandit_testbed(k: int, num_pulls: int, seed: int = 42) -> tuple:
    """
    Build a k-armed bandit testbed and simulate pulling each arm.
    
    Args:
        k: Number of arms
        num_pulls: Number of times to pull each arm
        seed: Random seed for reproducibility
    
    Returns:
        Tuple of (true_values, sample_means, optimal_arm)
    """
    np.random.seed(seed)
    true_values = [np.random.normal(0.0, 1.0) for _ in range(k)]
    sample_means = []
    for value in true_values:
        rewards = np.random.normal(value, 1.0, num_pulls)
        sample_means.append(np.mean(rewards))
    
    optimal_arm = int(np.argmax(true_values))
  
    return (np.round(true_values, 4).tolist(), np.round(sample_means, 4).tolist(), int(np.argmax(true_values)))



