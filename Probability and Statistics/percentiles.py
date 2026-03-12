import numpy as np

def calculate_latency_percentiles(latencies: list[float]) -> dict[str, float]:
    """
    Calculate P50, P95, and P99 latency percentiles.
    
    Args:
        latencies: List of latency measurements
    
    Returns:
        Dictionary with keys 'P50', 'P95', 'P99' containing
        the respective percentile values rounded to 4 decimal places
    """
    # Your code here
    percentiles = {'P50': 0.0, 'P95': 0.0, 'P99': 0.0}
    if not latencies:
        return percentiles
    else:
        n = len(latencies)
        k_50 = 0.5 * (n-1)
        k_50_floor = int(np.floor(k_50))
        k_50_ceil = int(np.ceil(k_50))
        position = latencies[k_50_floor] + (k_50-k_50_floor) * (latencies[k_50_ceil]-latencies[k_50_floor])
        percentiles['P50'] = round(position, 4)
        
        k_95 = 0.95 * (n-1)
        k_95_floor = int(np.floor(k_95))
        k_95_ceil = int(np.ceil(k_95))
        position = latencies[k_95_floor] + (k_95-k_95_floor) * (latencies[k_95_ceil]-latencies[k_95_floor])
        percentiles['P95'] = round(position, 4)
        
        k_99 = 0.99 * (n-1)
        k_99_floor = int(np.floor(k_99))
        k_99_ceil = int(np.ceil(k_99))
        position = latencies[k_99_floor] + (k_99-k_99_floor) * (latencies[k_99_ceil]-latencies[k_99_floor])
        percentiles['P99'] = round(position, 4)
        
        return percentiles


