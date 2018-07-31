def hemming_distance(value1, value2):
	hem = 0
	for i in range(0, len(value1)):
		if value1[i] != value2[i]:
			hem += 1
	print(hem)


hemming_distance('karolin', 'kathrin')
hemming_distance('karolin', 'kerstin')
