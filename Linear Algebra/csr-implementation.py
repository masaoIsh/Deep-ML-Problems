import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	rows, cols = np.nonzero(dense_matrix)
	vals = [dense_matrix[i][j] for i in range(len(dense_matrix)) for j in range(len(dense_matrix[0])) if dense_matrix[i][j]!=0]
	col_idx = list(cols)
	
	row_ptr = [0]
	counter = 0
	for i in range(len(dense_matrix)):
		for j in range(len(dense_matrix[0])):
			if dense_matrix[i][j] != 0:
				counter += 1
		row_ptr.append(counter)
		
	return (vals, col_idx, row_ptr)


