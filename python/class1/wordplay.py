def is_palindrome(word):
	if len(word) == 0 or len(word) == 1:
		return True
	elif word[0] == word[-1]:
		return is_palindrome(word[1:-1])	
	else:
		return False 

def is_abcedarian(word):
	if len(word) <=1:
		return True
	elif word[0] > word[1]:
		return False
	else:
		return is_abcedarian(word[1:])

#print(is_palindrome('kayak'))
#print(is_palindrome('hello'))

#print(is_abcedarian('abd'))
def check_words(func):
	fin = open('/Users/Corrector/Documents/Личное/США/UCSC/Python/words.txt')
	line = fin.readline()
	while line:
		wrd = line.strip()
		if is_palindrome(wrd):
			print(wrd)
		line = fin.readline()
check_words(is_palindrome)
