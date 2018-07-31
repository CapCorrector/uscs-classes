def dict_count(word):
	word = word.lower()
	d = {}
	for letter in word:
		if letter in d:
			d[letter] += 1
		else:
			d[letter] = 1
	return d

def reverse_lookup(d, value):
	result = []
	answ = None
	for k in d.keys():
		if d[k] == value:
			result.append(k)
	return result

def histogram(word):
	count = dict_count(word)
	occurance = remove_duplicates(count.values())
	occurance.sort()
	occurance.reverse()
	result = {}
	for occur in occurance:
		result[occur] = reverse_lookup(count, occur)
	return result

def remove_duplicates(orig):
	result = []
	for elem in orig:
		if elem not in result:
			result.append(elem)
	return result
			
	

word = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
#count = dict_count(word)
#print(count)
#print(reverse_lookup(count, 9))
#print(reverse_lookup(count, 6))	
#print(reverse_lookup(count, 8))
result = histogram(word)
print(result)
