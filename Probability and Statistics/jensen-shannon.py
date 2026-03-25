import numpy as np

def jensen_shannon_divergence(P: list[float], Q: list[float]) -> float:
	"""
	Compute the Jensen-Shannon Divergence between two probability distributions.
	
	Args:
		P: First probability distribution
		Q: Second probability distribution
	
	Returns:
		Jensen-Shannon Divergence value
	"""
	# Your code here
	M = [0.5 * (P[i]+Q[i]) for i in range(len(P))]
	
	kl_pm = 0
	for i in range(len(P)):
		if P[i] == 0 or M[i] == 0:
			continue
		kl_pm += P[i] * np.log(P[i]/M[i])
	
	kl_qm = 0
	for j in range(len(Q)):
		if Q[j] == 0 or M[j] == 0:
			continue
		kl_qm += Q[j] * np.log(Q[j]/M[j])
	
	return 0.5*kl_pm + 0.5*kl_qm

