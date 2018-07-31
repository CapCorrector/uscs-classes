def grades(score):
	if score >= 90:
		return 'A'
	elif score >= 80:
		return 'B'
	elif score >= 70:
		return 'C'
	elif score >= 60:
		return 'D'
	else:
		return 'F'

fullgr = []
fin = open('grades.txt')
line = fin.readline()
while line:
	line = line.strip()
	fullgr.append(line.split(','))
	line = fin.readline()
fin.close()
print(fullgr)
for num in fullgr:
#	score_sum = 0
#	for score in num[2:]:
#		score_sum += int(score)
#	score_avg = score_sum / 4
	score_avg = sum(map(int, num[2:])) / len (num[2:])
	print(num[0] + ': ' + str(score_avg) + '\t' + grades(score_avg))
