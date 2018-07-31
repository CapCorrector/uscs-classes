def get_anagram(filename):
	anagram_dict = {}
	fin = open(filename)
	for line in fin:
		word = line.strip()
		signature = get_signature(word)
		if signature in anagram_dict:
			anagram_dict[signature].append(word)
		else:
			anagram_dict[signature] = [word]
		return get_top_five_anagrams(anagram_dict)

def get_signature(word):
	return ''.join(sorted(word))

def get_top_five_anagrams(anagram_dict):
	return sorted(anagram.dict.values(), key=lambda v: len(v), reverse=True)[:5]


get_anagram('words.txt')

