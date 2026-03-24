import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
	"""
	Compute entropy of P and cross-entropy between P and Q.
	
	Args:
		P: True probability distribution
		Q: Predicted probability distribution
	
	Returns:
		Tuple of (entropy H(P), cross-entropy H(P,Q))
	"""
	# Your code here
	num_zeros = 0
	for number in P:
		if number == 0.0:
			num_zeros += 1
	if num_zeros == len(P)-1:
		entropy = 0.0
	else:
		entropy = 0
		for i in range(len(P)):
			entropy += P[i]*np.log(P[i])
		entropy *= -1

	cross_entropy = 0
	for i in range(len(Q)):
		cross_entropy += P[i]*np.log(Q[i])
	
	cross_entropy *= -1

	return (entropy, cross_entropy)




