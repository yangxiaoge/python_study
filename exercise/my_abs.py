def my_abs(a):
	if not isinstance(a,(int,float)):
		raise TypeError('bad operand type')
	if a>=0:
		return a
	else:
		return -a