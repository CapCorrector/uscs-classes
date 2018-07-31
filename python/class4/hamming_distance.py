def hamming_distance(str1, str2):
	distance = 0
#	for index in range(len(str1)):
#		if str1[index] != str2[index]:
#			distance += 1
	
	for x,y in zip(str1,str2):
		if x != y:
			distance += 1
	return distance

print(hamming_distance('karolin', 'kathrin'))
