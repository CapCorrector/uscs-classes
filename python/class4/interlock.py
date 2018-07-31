def binary_search(word, words):
	low = 0
	high = len(words)-1
	while low <= high:
		mid = (low+high) //2
		if word == words[mid]:
			return True
		elif word < words[mid]:
			high = mid -1
		else:
			low = mid +1
	return False
		
	

def get_interlock(filename):
	words = []
	fin = open(filename)
	for line in fin:
		words.append(line.strip())
	result = []
	words_set = set(words)
	for word in words:
		even_part = word[::2]
		odd_part = word[1::2]
		#if even_part in words and odd_part in words:
		#if binary_search(even_part, words) and binary_search(odd_part, words):
		if even_part in words_set and odd_part in words_set:
			result.append(word)
	return result

result = get_interlock('words.txt')
print(len(result))
print(result)
