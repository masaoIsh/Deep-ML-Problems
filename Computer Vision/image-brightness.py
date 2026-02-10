
def calculate_brightness(img):
	# Write your code here
	if not img:
		return -1
	
	row_length = len(img[0])
	total = 0
	counter = 0
	
	for i in range(len(img)):
		for j in range(len(img[0])):
			if len(img[i]) != row_length:
				return -1
			elif (img[i][j] > 255) or (img[i][j]) < 0:
				return -1
			else:
				total += img[i][j]
				counter += 1
	
	return total / counter 




	

