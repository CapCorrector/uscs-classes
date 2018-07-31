numbers = [1, 4, 9, 8, 4]
#squares = list(map(lambda n: n**2, numbers))
squares = [n**2 for n in numbers]
even_squares = [n**2 for n in numbers if n%2 == 0]

names = ['Alice', 'Bob', 'david', 'eRIC']
formated_names = [name[0].upper() + name[1:].lower() for name in names]

emails = ['alice 12@gmail.com', 'alice123', 'bob@abc.com', 'alice@abc.com']
valid_emails =[email for email in emails if ' ' not in email and '@' in email]

dup_names = ['Alice', 'BOB', 'david', 'eRIC', 'alice', 'bob']
unique_names = {name[0].upper() + name[1:].lower() for name in dup_names}

letter_freq = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
valid_freq = {letter.lower(): letter_freq.get(letter.lower(), 0) + letter_freq.get(letter.upper(), 0) for letter in letter_freq.keys()}

print(squares)
print(even_squares)
print(formated_names)
print(valid_emails)
print(unique_names)
print(valid_freq)
