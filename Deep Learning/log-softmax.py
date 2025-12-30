import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	scores = np.array(scores)
    output = [(number - np.log(sum([np.exp(score) for score in scores]))) for number in scores]
    
    return output
