def find_kw(word, key)
	pos = word.find(key)
	while pos >= 0
a = input('''Hi let's talk\n''')
while a.lower() != 'bye':
	if len(a.strip()) == 0:
		print('Say something')
	elif a.lower().find('cat') >= 0 or a.lower().find('dog') >=0:
		pass
	else:
		print(a)
	a = input('input \'text\'\n')
