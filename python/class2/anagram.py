def is_anagram(word1, word2):
	return sorted(word1) == sorted(word2)

print(is_anagram('post', 'stop'))
print(is_anagram('pots', 'post'))
print(is_anagram('hello', 'world'))
