import numpy as np

def determinant_twobytwo(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def cross_product(a, b):
    # Your code here
    return [determinant_twobytwo([[a[1], a[2]], [b[1], b[2]]]), -1*determinant_twobytwo([[a[0], a[2]], [b[0], b[2]]]), determinant_twobytwo([[a[0], a[1]], [b[0], b[1]]])]


