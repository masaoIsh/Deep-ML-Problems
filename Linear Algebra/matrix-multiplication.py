def matrix_transpose(c:list[list[int|float]]):
    n = len(c[0])
    m = len(c)
    d = [[0 for i in range(m)] for j in range(n)]
    for i in range(len(d)):
        for j in range(len(d[0])):
            d[i][j] = c[j][i]

    return d


def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[0]) != len(b):
        return -1
    
    matrix = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    #print(f"The matrix is {len(matrix)} by {len(matrix[0])}")
    #print(matrix)
    b_t = matrix_transpose(b)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = sum([a[i][k]*b_t[j][k] for k in range(len(a[i]))])

    return matrix
