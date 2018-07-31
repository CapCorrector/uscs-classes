def pi_seq():
	'''get the sequence to simulate pi'''
	result = 0
	denominator = 1
	sign = 1
	while True:
		result += sign/denominator
		yield result * 4
		sign *= -1
		denominator += 2

def firstn(g, n):
	'''print the first n items from g as a generator'''
	for i in range(n):
		print(next(g))

def accelerator(g):
	s0 = next(g)
	s1 = next(g)
	s2 = next(g)
	while True:
		yield s2 - (s2 - s1)**2 / (s0 -2*s1 +s2)
		s0, s1, s2 = s1, s2, next(g)

if __name__ == '__main__':
	firstn(pi_seq(), 100)
	firstn(accelerator(pi_seq()), 100)
