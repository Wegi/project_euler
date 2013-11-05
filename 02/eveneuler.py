def calc_euler():
	fibs1 = 1
	fibs2 = 1
	sum = 2
	fibsnew = fibs2 + fibs1
	fibs1 = fibs2
	fibs2 = fibsnew
	
	while fibsnew < 4000000:
		fibsnew = fibs2 + fibs1
		fibs1 = fibs2
		fibs2 = fibsnew
		if fibsnew%2 == 0:
			sum += fibsnew
	
	print sum
	
calc_euler()