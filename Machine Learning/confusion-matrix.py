
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	tp = 0
	fp = 0
	fn = 0
	tn = 0
	
	for i in range(len(data)):
		#print(f"This is for data point {data[i]}")
		#print(f"Data[i][0] is {data[i][0]}")
		if data[i][0]==1 and data[i][1]==1:
			#print("Add one to tp")
			tp += 1
		elif data[i][0]==0 and data[i][1]==1:
			#print("Add one to fp")
			fp += 1
		elif data[i][0]==1 and data[i][1]==0:
			#print("Add one to fn")
			fn += 1
		else:
			#print("Add one to tn")
			tn += 1
	
	#confusion = [[tn, fp], [fn, tp]]
	confusion = [[tp, fn], [fp, tn]]


	return confusion

