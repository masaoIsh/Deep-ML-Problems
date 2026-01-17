import numpy as np

def rref(matrix):
	matrix = matrix.astype(float)
    n, m = matrix.shape
    for i in range(n):
        if matrix[i, i] == 0:
            row_indices = np.nonzero(matrix[i:, i])[0] + i
            if len(row_indices) == 0:
                continue
            matrix[[i, row_indices[0]]] = matrix[[row_indices[0], i]]
        matrix[i] = matrix[i] / matrix[i, i]
        for j in range(n):
            if i != j:
                matrix[j] -= matrix[i]*matrix[j, i]
    
    #print(f"Matrix now: {matrix}")
    num_zero_rows = 0
    for k in range(n-1):
        if len(np.nonzero(matrix[k])[0]) == 0:
            matrix[[k, n-1-num_zero_rows]] = matrix[[n-1-num_zero_rows, k]]
            num_zero_rows+=1
            #print(f"Matrix after swap{k}: {matrix}")
    return matrix

