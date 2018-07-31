def lev(word1, word2):
	word1 = word1.lower()
	word2 = word2.lower()
	if word1 == '' or word2 == '':
		return max(len(word1), len(word2))
	if word1[-1] == word2[-1]:
		distance = 0
	else:
		distance = 1
	possible_distance1 = lev(word1[:-1], word2) + 1
	possible_distance2 = lev(word1, word2[:-1]) + 1
	possible_distance3 = lev(word1[:-1], word2[:-1]) + distance
	
	return min(possible_distance1, possible_distance2, possible_distance3)

def lev_memo(word1, word2):
	word1 = word1.lower()
	word2 = word2.lower()
	if word1 == '' or word2 == '':
                return max(len(word1), len(word2))
	if word1[-1] == word2[-1]:
		distance = 0
	else:
		distance = 1

	possible_distance1 = calc_lev(word1[:-1], word2, 1)
	possible_distance2 = calc_lev(word1, word2[:-1], 1)
	possible_distance3 = calc_lev(word1[:-1], word2[:-1], distance)

def calc_lev(part1, part2, distance):
	result = memo_search(part1, part2)
	if result == None:
		result = lev_memo(part1, part2)
		memo[part1 + ':' + part2] = result
	return result + distance

def memo_search(part1, part2):
	key1 = part1 + ':' + part2
	key2 = part2 + ':' + part1
	if key1 in memo:
		return memo[key1]
	if key2 in memo:
		return memo[key2]
	return None

memo = {}

print(lev_memo('Python', 'Peithen'))
print(lev_memo('resettacode', 'raisethysword'))
