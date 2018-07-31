def print_digit(number):
	while number > 0:
		digit = number % 10
		print(digit)
		number //= 10

#print_digit(12341)
def is_self_divisor(number):
	target = number
	while number > 0:
		digit =number % 10
		if digit == 0 or target % digit != 0:
			return False
		number //= 10
	return True
	
#for number in range(1, 1001):
#	if is_self_divisor(number):
#		print(number)	


import math

#int(math.log10(1485))


def is_armstr_num(number):
	import math
	target = number
	digit_sum = 0
	num_len = int(math.log10(number))+1
	while number > 0:
		digit = number % 10
		digit_sum += digit ** num_len
		number //= 10 
	return digit_sum == target	

for number in range(1, 10001):
       if is_armstr_num(number):
               print(number)
