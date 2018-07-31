names = ['Alice', 'Bob', 'Charles']
ages = [18, 20, 15]
gender = ['F', 'M', 'M']
school = ['Stanford', 'UCSC', 'San Jose State']

print(list(zip(names, ages, gender, school)))
print(dict(zip(names, zip(ages, gender, school))))
