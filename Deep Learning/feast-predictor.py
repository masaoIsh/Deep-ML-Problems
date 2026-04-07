import math

def thanksgiving_dish_predictor(preference_scores: list[float]) -> list[float]:
	"""
	Predict the probability of choosing each Thanksgiving dish using softmax.
	
	Args:
		preference_scores: List of preference scores for each dish
		(e.g., [turkey_score, stuffing_score, cranberry_score, pie_score])
		
	Returns:
		List of probabilities for each dish
	"""
	# Your code here
	denominator = sum([math.exp(preference_scores[i]) for i in range(len(preference_scores))])
	return [math.exp(preference_scores[i])/denominator for i in range(len(preference_scores))]
