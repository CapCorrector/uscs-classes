def friends_each_and_avg(links):
	count = {}
	for i in [x for t in links for x in t]:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1
	sorted_friends = sorted(count.items(), key = lambda entry: entry[1], reverse=True)
	for friend in sorted_friends:
		print(friend[0], ' has ', friend[1], ' friends')
	print('Avg frirnds qty is ', sum(count.values())/len(count))

def first_level_friends(id, links):
	flf = []
	for link in links:
		if link[0] == id:
			flf.append(link[1])
		elif link[1] == id:
			flf.append(link[0])
	return flf

def second_level_friends(id, links):
	slf_unfiltered = []
	flf = first_level_friends(id, links)
	for friend in flf:
		slf_unfiltered.extend(first_level_friends(friend, links))
	slf = list(set([x for x in slf_unfiltered if x not in flf and x != id]))
	return slf

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
friends_each_and_avg(friendships)

for id in range(0,10):
	print(id,'\'s friends are:', second_level_friends(id, friendships))
