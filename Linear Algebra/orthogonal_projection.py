
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	L_norm_squared = 0
    dot_product = 0
    for i in range(len(L)):
        L_norm_squared += L[i]**2
        dot_product += v[i]*L[i]
    magnitude = dot_product / L_norm_squared
    for i in range(len(L)):
        L[i] *= magnitude
    return L

