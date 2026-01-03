import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities = []
    mse = 0

    def sigmoid(z):
        return 1 / (1+math.exp(-1*z))
    
    for data in features:
        z = 0
        for i in range(len(data)):
            z+=data[i]*weights[i]
        z+=bias
        probabilities.append(round(sigmoid(z), 4))
    
    predictions = [int(probability>0.5) for probability in probabilities]

    for k in range(len(probabilities)):
        mse += (probabilities[k]-labels[k]) ** 2
    mse = round(mse / len(predictions), 4)

    return (probabilities, mse)

    
    
    




    return probabilities, mse
