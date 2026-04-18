import numpy as np

def optimistic_greedy_bandit(
    true_rewards: list,
    initial_q: float,
    n_steps: int,
    step_size: float
) -> tuple:
    """
    Simulate a greedy bandit agent with optimistic initialization.
    
    Args:
        true_rewards: List of true deterministic rewards for each arm
        initial_q: Optimistic initial Q-value for all arms
        n_steps: Number of steps to simulate
        step_size: Constant step-size (alpha) for Q-value updates
    
    Returns:
        Tuple of (Q_values, action_counts) where Q_values is a list of
        floats rounded to 4 decimal places, and action_counts is a list of ints.
    """
    # Your code here
    true_rewards = np.array(true_rewards, dtype=float)
    # initial_q = np.array(initial_q, dtype=float)
    counts = {i: 0 for i in range(len(true_rewards))}

    q_values = [initial_q for _ in range(len(true_rewards))]
    for i in range(n_steps):
        action = np.argmax(q_values)
        # action_index = q_values.tolist().index(action)
        reward = true_rewards[action]
        counts[action] += 1
        q_values[action] = q_values[action] + step_size * (reward - q_values[action])

    q_values = [round(value, 4) for value in q_values]

    return (q_values, list(counts.values()))

