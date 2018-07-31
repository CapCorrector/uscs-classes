def firstn(g, n):
	for i in range(n):
		print(next(g))

def numbers_from(start):
	while True:
		yield start
		start += 1

def numbers_not_by_n(nat_gen, n):
	for i in nat_gen:
		if i % n != 0:
			yield i 

def prime(seq):
	while True:
		prime = next(seq)
		yield prime
		seq = numbers_not_by_n(seq, prime)

if __name__ == '__main__':
	firstn(numbers_not_by_n(numbers_from(2), 2), 10)	
	print('=' *40)
	firstn(prime(numbers_from(2)), 100)
