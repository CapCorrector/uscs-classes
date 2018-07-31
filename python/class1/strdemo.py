def encr(word, offset):
	ans = ''
	charset = 'abcdefghijklmnopqrstuvwxyz'
	for let in word:
		orind = charset.find(let)
		newind = (orind + offset) % len(charset)
		ans +=  charset[newind]
	return ans

def encr2(word, offset):
	offset %= 26
	charset = 'abcdefghijklmnopqrstuvwxyz'
	lookup_table = charset[offset:] + charset[:offset]
	ans = ''
	for let in word:
		ind = charset.find(let)
		if ind == -1:
			ans += let
		else:
			ans += lookup_table[ind]
	return ans

print(encr('cheer', 7))
print(encr2('hello world!', 13))
