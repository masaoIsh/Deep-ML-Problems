import numpy as np

def mutual_information(joint_prob: list[list[float]]) -> float:
	"""
	Compute the mutual information between two random variables.
	
	Args:
		joint_prob: 2D joint probability distribution P(X,Y)
	
	Returns:
		Mutual information I(X;Y)
	"""
	# Your code here
	joint_prob = np.array(joint_prob, dtype=float)
	marginal_x = [sum(the_row) for the_row in joint_prob]
	marginal_y = [sum(the_row) for the_row in joint_prob.T]

	mutual = 0
	for i in range(len(marginal_x)):
		for j in range(len(marginal_y)):
			if joint_prob[i][j] == 0.0:
				continue
			mutual += joint_prob[i][j]*np.log(joint_prob[i][j]/(marginal_x[i]*marginal_y[j]))
	
	return mutual

