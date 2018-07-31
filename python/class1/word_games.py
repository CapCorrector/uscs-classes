def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

def is_abcedarian(word):
    if len(word) <= 1:
        return True
    elif word[0] > word[1]:
        return False
    else:
        return is_abcedarian(word[1:])

#print('{} is palindrome: {}'.format('kayak', is_palindrome('kayak')))
#print('{} is palindrome: {}'.format('hello', is_palindrome('hello')))

#print('{} is abcedarian: {}'.format('accept', is_abcedarian('accept')))
#print('{} is abcedarian: {}'.format('brother', is_abcedarian('brother')))

def check_words(check_func):
    fin = open('words.txt')

    line = fin.readline()

    while line:
        word = line.strip()

        if check_func(word):
            print(word)
        
        line = fin.readline()

#check_words(is_palindrome)
#check_words(is_abcedarian)

def find_longest_word(check_func):
    longest_word_so_far = ''
    
    fin = open('words.txt')

    line = fin.readline()

    while line:
        word = line.strip()

        if check_func(word) and len(word) >= len(longest_word_so_far):
            longest_word_so_far = word        
        
        line = fin.readline()

    return longest_word_so_far

print('Longest palindrome: {}'.format(find_longest_word(is_palindrome)))
print('Longest abcedarian: {}'.format(find_longest_word(is_abcedarian)))
