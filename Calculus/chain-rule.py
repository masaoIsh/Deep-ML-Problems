import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	mapping = {
		'square': (lambda t: t**2, lambda t: 2*t),
		'sin': (lambda t: np.sin(t), lambda t: np.cos(t)),
		'exp': (lambda t: np.exp(t), lambda t: np.exp(t)),
		'log': (lambda t: np.log(t), lambda t: 1 / t)
	}

	values = [x]
	for function in reversed(functions):
		to_eval, foo = mapping[function]
		values.append(to_eval(values[-1]))
	
	answer = 1
	for i, function in enumerate(reversed(functions)):
		foo, deriv = mapping[function]
		answer *= deriv(values[i])
	
	return float(answer)

		

