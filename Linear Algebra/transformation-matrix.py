import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    B = np.array(B)
    C = np.array(C)
    inv_c = np.linalg.inv(C)

    return np.matmul(inv_c, B)
