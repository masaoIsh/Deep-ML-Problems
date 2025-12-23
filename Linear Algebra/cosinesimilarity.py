
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
    v1_squaredsum = 0
    for i in range(len(v1)):
        v1_squaredsum += v1[i]**2
    v2_squaredsum = 0
    for i in range(len(v2)):
        v2_squaredsum += v2[i]**2

    dot_product = np.dot(v1, v2)
    v1_norm = np.sqrt(v1_squaredsum)
    v2_norm = np.sqrt(v2_squaredsum)
    
    return round((dot_product / (v1_norm * v2_norm)), 3)

