cubed_numbers = [5, 13, 4, 6]
squared_numbers = [11, 2, 6, 17]
unit_numbers = [9, 8, 4, 18]

result = list(map(lambda a,b,c: a**3+b**2+c, cubed_numbers, squared_numbers, unit_numbers))
print(result)
