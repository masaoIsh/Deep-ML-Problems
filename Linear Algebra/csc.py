import numpy as np

def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	dense_matrix = np.array(dense_matrix)
    dense_matrix_t = dense_matrix.T
    values = []
    for i in range(len(dense_matrix_t)):
        for j in range(len(dense_matrix_t[0])):
            if dense_matrix_t[i][j] != 0:
                values.append(dense_matrix_t[i][j])
    
    row_idx = list(np.nonzero(dense_matrix_t)[1])
    
    col_ptr = [0]
    counter = 0
    for i in range(len(dense_matrix_t)):
        for j in range(len(dense_matrix_t[0])):
            if dense_matrix_t[i][j] != 0:
                counter+=1
        col_ptr.append(counter)

    return (values, row_idx, col_ptr)
        


