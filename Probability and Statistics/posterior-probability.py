def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	the_sum = sum([(priors[i]*likelihoods[i]) for i in range(len(priors))])
    return [((priors[i]*likelihoods[i]) / the_sum) for i in range(len(priors))]
