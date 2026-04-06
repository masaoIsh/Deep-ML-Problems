import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    # Your code here
    if len(p) != len(q):
        return 0.0
    
    coef = np.sum([np.sqrt(p[i]*q[i]) for i in range(len(p))])
    return -1 * np.log(coef) if coef != 0 else 0.0


