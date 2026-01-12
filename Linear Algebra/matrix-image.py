import numpy as np

def rref(A):
    A = A.astype(np.float32)
    n, m = A.shape
    
    for i in range(n):
        if A[i, i] == 0:  #swap rows
            row_index = np.nonzero(A[i:, i])[0] + i
            if len(row_index) == 0:
                continue
            A[[i, row_index[0]]] = A[[row_index[0], i]]
        A[i] = A[i] / A[i, i]
        for j in range(n):
            if i!=j:
                A[j] -= A[i]*A[j, i] 
    
    return A


def pivot_columns(A):
    #take in rref matrix as input
    pivots = []
    for i in range(A.shape[0]):
        pivot_index = np.nonzero(A[i, :])[0]
        if len(pivot_index) > 0:
            pivots.append(pivot_index[0])
    
    return pivots

def matrix_image(A):
	# Write your code here
	rref_A = rref(A)
    pivots = pivot_columns(rref_A)
    image = A[:, pivots]

    return image

