def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    trace = sum([matrix[i][i] for i in range(len(matrix))])

    def determinant(mat):
        # base case
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        det = 0
        for i in range(len(mat[0])):
            # minor, remove row 1 and column i
            minor = [[mat[k][j] for j in range(len(mat[0])) if j != i] for k in range(1, len(mat))]
            det += ((-1) ** i) * mat[0][i] * determinant(minor)
        return det

    det_val = determinant(matrix)
    return (det_val, trace)
