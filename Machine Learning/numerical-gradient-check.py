import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    approx_grad = []
    for i in range(x.shape[0]):
        perturb_one = x.copy()
        perturb_one[i] += epsilon
        perturb_two = x.copy()
        perturb_two[i] -= epsilon
        approx_grad.append((f(perturb_one) - f(perturb_two))/(2*epsilon))
    numerical_grad = np.array(approx_grad).astype(float)

    analytical_norm = np.linalg.norm(analytical_grad)
    numerical_norm = np.linalg.norm(numerical_grad)
    norm_sum = analytical_norm + numerical_norm

    numerator = np.linalg.norm(numerical_grad - analytical_grad)
    relative_error = numerator / norm_sum if norm_sum != 0 else 0.0

    return (numerical_grad, relative_error)
