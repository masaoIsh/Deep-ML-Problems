import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
	return 0.5 * (((mu_p-mu_q)**2)/sigma_q**2 + sigma_p**2/sigma_q**2 - np.log(sigma_p**2/sigma_q**2) - 1)

