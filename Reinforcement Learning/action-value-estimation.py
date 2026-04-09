def sample_average_action_values(k: int, actions: list, rewards: list) -> tuple:
    """
    Estimate action values using sample averaging.
    
    Args:
        k: Number of possible actions (labeled 0 to k-1)
        actions: List of actions taken at each time step
        rewards: List of rewards received at each time step
        
    Returns:
        Tuple of (Q, N) where Q is estimated values and N is selection counts
    """
    action_dict = {i: 0 for i in range(k)}
    count_dict = {i: 0 for i in range(k)}
    for j in range(len(actions)):
        action_dict[actions[j]] = action_dict[actions[j]] + rewards[j]
        count_dict[actions[j]] = count_dict[actions[j]] + 1
    
    
    action_vals = list(action_dict.values())
    count_vals = list(count_dict.values())
    Q = [round(action_vals[i]/count_vals[i], 4) if count_vals[i] != 0 else 0.0 for i in range(len(action_vals))]

    return (Q, count_vals)



    



