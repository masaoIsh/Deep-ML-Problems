import numpy as np

def covariance_from_joint_pmf(x_values: list, y_values: list, joint_pmf: np.ndarray) -> float:
    """
    Compute the covariance of X and Y from their joint PMF.
    
    Args:
        x_values: List of possible values for X
        y_values: List of possible values for Y
        joint_pmf: 2D numpy array where joint_pmf[i][j] = P(X=x_values[i], Y=y_values[j])
    
    Returns:
        Covariance of X and Y as a float
    """
    # Your code here
    e_xy = 0
    for i in range(len(x_values)):
        for j in range(len(y_values)):
            e_xy += x_values[i]*y_values[j]*joint_pmf[i][j]
    
    marginal_x = [sum(row) for row in joint_pmf]
    e_x = 0
    for i in range(len(x_values)):
        e_x += x_values[i]*marginal_x[i]

    marginal_y = [sum(row) for row in joint_pmf.T]
    e_y = 0
    for i in range(len(y_values)):
        e_y += y_values[i]*marginal_y[i]

    cov = e_xy - e_x*e_y

    return cov



