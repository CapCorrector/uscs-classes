def table_loop():
	pass
	res = []
	for x in range(1, 10):
		res.append([])
		for y in range(1, x+1):
			res[x-1].append((str(y) + ' * ' + str(x) + ' = ' + str(x*y)))
		print('	'.join((res[x-1])))

def table_comp():
	resc = [[str(y) + ' * ' + str(x) + ' = ' + str(x*y) for y in range(1, x+1)] for x in range(1,10)]
	for x in range(0, 9):
		print('	'.join(resc[x]))

if __name__ == '__main__':
	table_loop()
	table_comp()
