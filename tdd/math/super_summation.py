def super_summation(*args):
	''' sums up the arguments
	'''
	total = 0
	for i in args:
		if isinstance(i,list):
			total += super_summation(*i)
		else :
			total += i
	return total
