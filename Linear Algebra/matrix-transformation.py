import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	try:
        T_inv = np.linalg.inv(T)
    except np.linalg.LinAlgError:
        return -1
    
    try:
        S_inv = np.linalg.inv(S)
    except np.linalg.LinAlgError:
        return -1
    
    
    transformed_matrix = np.matmul(T_inv, A)
    transformed_matrix = np.matmul(transformed_matrix, S)
    
    return transformed_matrix
