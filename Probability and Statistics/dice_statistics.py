def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	expected_value = 0
    for i in range(1,n+1):
        expected_value += i*(1/n)
    
    variance = 0
    for i in range(1, n+1):
        variance += ((i-expected_value)**2)*(1/n)

    return (expected_value, variance)
