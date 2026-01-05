
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	mean = np.mean(y_true)
    sst = np.sum([(y_true[i]-mean)**2 for i in range(len(y_true))])
    ssr = np.sum([(y_pred[i]-y_true[i])**2 for i in range(len(y_pred))])

    return 1 - (ssr / sst)


