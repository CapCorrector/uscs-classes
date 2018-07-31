#def convert_temperature(tf):
#	return (tf-32) * 5 / 9

#temperatures = list(range(0, 101, 10))

#print(temperatures)


#conv = list(map(lambda tf: (tf-32) * 5 / 9, list(range(0, 101, 10))))


#print(conv)

temperatures = '10,20,40,67,23'
temp_values = list(map(int, temperatures.split(',')))
conv = list(map(lambda tf: (tf-32) * 5 / 9, temp_values))
print(temp_values)
print(conv)
print(list(map(lambda tf: (int(tf)-32) * 5 / 9, temp_values, temperatures.split(','))))
