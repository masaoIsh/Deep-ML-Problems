import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
    probabilities = [(math.exp(scores[i]) / sum([math.exp(number) for number in scores])) for i in range(len(scores))]
	
    return probabilities
