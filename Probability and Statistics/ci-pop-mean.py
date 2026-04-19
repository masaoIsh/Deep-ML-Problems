import numpy as np
from scipy import stats

def confidence_interval(data: list[float], confidence_level: float = 0.95) -> dict:
	"""
	Calculate confidence interval for population mean.
	
	Args:
		data: Sample data
		confidence_level: Confidence level (default 0.95)
	
	Returns:
		Dictionary containing:
		- mean: Sample mean (point estimate)
		- standard_error: Standard error of the mean
		- margin_of_error: Margin of error
		- lower_bound: Lower bound of CI
		- upper_bound: Upper bound of CI
		- confidence_level: Confidence level used
	"""
	# Your code here
	n = len(data)
	mean = np.mean(data)
	# var = np.var(data)
	std = np.std(data, ddof=1)
	standard_error = std / np.sqrt(n)
	# critical value computation
	df = n - 1
	alpha = 1 - confidence_level
	critical_value = stats.t.ppf(1-alpha/2, df)
	
	margin_of_error = standard_error * critical_value
	lower_bound = mean - margin_of_error
	upper_bound = mean + margin_of_error
	
	val = {'mean': mean, 'standard_error': standard_error, 'margin_of_error': margin_of_error, 'lower_bound': lower_bound, 'upper_bound': upper_bound, 'confidence_level': confidence_level}

	return val
