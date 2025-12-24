import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    data = np.array(data)

    counts = {}
    for i in range(len(data)):
        if data[i] in counts:
            counts[data[i]] += 1
        else:
            counts[data[i]] = 1
    

    descriptive_stats_dic = {'mean': np.mean(data), 'median': np.median(data), 'mode': max(counts, key=counts.get), 'variance': np.var(data), 'standard_deviation': np.std(data), '25th_percentile': np.percentile(data, 25), '50th_percentile': np.percentile(data, 50), '75th_percentile': np.percentile(data, 75), 'interquartile_range': (np.percentile(data, 75)-np.percentile(data, 25))}
    return descriptive_stats_dic

