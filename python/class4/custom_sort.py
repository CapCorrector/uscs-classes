words = ['collar', 'scholar', 'absolute', 'church', 'check', 'disclose', 'film', 'put', 'conclusion', 'welfare']

def sort_by_length(words):
	records = []
	for word in words:
		records.append((len(word), word))
	records.sort()
	sorted_words = list(map(lambda t: t[-1],records))
	return sorted_words

def sort_by_last_letter(words):
	records = []
	index = 0
	for word in words:
		records.append(((word[-1],index), word))
		index += 1
	records.sort()
	sorted_words = list(map(lambda t: t[-1],records))
	return sorted_words

def sort_by(words, sortfunc, reverse=False):
	records = []
	index = 0
	for word in words:
		records.append(((sortfunc(word), index), word))
		index += 1
	records.sort()
	if reverse:
		records.reverse()
	sorted_words = list(map(lambda t: t[-1],records))
	return sorted_words

#print(sort_by_length(words))
#print(sort_by_last_letter(words))
print(sort_by(words, len, True))
print(sort_by(words, lambda word: word[-1]))

# built-in Python sort
print(sorted(words, key=len, reverse=True))
print(sorted(words, key=lambda word: word[-1], reverse=True))
print(sorted(words, key=lambda word: (word[-1], words.index(word)), reverse=True))
