def cumulativesum(arr):
	cursum = 0
	ret = []
	for num in arr:
		cursum += num
		ret.append(cursum)
	return ret

result = cumulativesum([1, 2,3])
print(result)
