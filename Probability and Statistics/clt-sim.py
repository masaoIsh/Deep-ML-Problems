import numpy as np

def simulate_clt(distribution: str, n: int, runs: int = 10000, seed: int = 42) -> dict:
    """
    Simulate the Central Limit Theorem.

    Args:
        distribution (str): The distribution to sample from ('uniform', 'exponential', 'bernoulli').
        n (int): Sample size.
        runs (int): Number of repeated experiments.
        seed (int): Random seed for reproducibility.

    Returns:
        dict: {'mean': float, 'std': float} of the standardized sample means.
    """
    np.random.seed(seed)
    # Your implementation here
    def compute_std(the_list, the_mean):
        squared_sum = 0
        for i in range(len(the_list)):
            squared_sum += (the_list[i]-the_mean)**2
        squared_sum_mean = squared_sum / (len(the_list))

        return np.sqrt(squared_sum_mean)

    if distribution == 'uniform':
        mu = 0.5
        sigma = np.sqrt(1 / 12)
        values = []
        for i in range(runs):
            sample = np.random.uniform(0, 1, size=n)
            sample_mean = sum(sample) / n
            standardize = (sample_mean - mu) / (sigma/np.sqrt(n))
            values.append(standardize)
        mean = sum(values) / runs
        std = compute_std(values, mean)

        return {'mean': mean, 'std': std}

    
    if distribution == 'exponential':
        mu = 1
        sigma = 1
        values = []
        for i in range(runs):
            sample = np.random.exponential(1, size=n)
            sample_mean = sum(sample) / n
            standardize = (sample_mean - mu) / (sigma/np.sqrt(n))
            values.append(standardize)
        mean = sum(values) / runs
        std = compute_std(values, mean)
        return {'mean': mean, 'std': std}
    
    if distribution == 'bernoulli':
        mu = 0.3
        sigma = np.sqrt(0.3 * 0.7)
        values = []
        for i in range(runs):
            sample = (np.random.rand(n) < 0.3).astype(int)
            sample_mean = np.mean(sample)
            standardized = (sample_mean - mu) / (sigma / np.sqrt(n))
            values.append(standardized)
        mean = np.mean(values)
        std = np.std(values)
        return {'mean': float(mean), 'std': float(std)}
    
    else:
        return None
