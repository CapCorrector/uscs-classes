def cumulativesum(arr):
	cursum = 0
	ret = []
	for num in arr:
		cursum += num
		ret.append(cursum)
	return ret

def promote_count(before, after):
	cum_before = cumulativesum(before)
	cum_after = cumulativesum(after)
#	diff = []
#	for inx in range(len(before)):
#		diff.append(cum_after[inx] - cum_before[inx])
	
#	return diff
	return list(map(lambda a, b: a - b, cum_after, cum_before))

before = [26, 33, 19, 30]
after = [53, 8, 28, 20]

#promote = promote_count(before, after)
#print(promote)

print(list(map(lambda a, b: a - b, cumulativesum(after), cumulativesum(before))))
