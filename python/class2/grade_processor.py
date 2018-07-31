def grade(score):
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

fin = open('grades.txt')

students = []

line = fin.readline()
while line:
    line = line.strip()
    students.append(line.split(','))
    line = fin.readline()

fin.close()

for student in students:
    score_sum = 0
    for score in student[2:]:
        score_sum += int(score)
    score_ave = score_sum / 4
    print(student[0] + ': ' + str(score_ave) + '\t' + grade(score_ave))
