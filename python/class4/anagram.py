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

    # return top-5 anagram lists
    return get_top_five_anagrams(anagram_dict)

def get_signature(word):
    return ''.join(sorted(word))

def get_top_five_anagrams(anagram_dict):
    return sorted(anagram_dict.values(), key=len, reverse=True)[:5]


top_5 = get_anagram('words.txt')
for ana in top_5:
    print(ana)
