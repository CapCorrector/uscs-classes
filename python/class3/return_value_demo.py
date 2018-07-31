def min_max(*numbers):
	return min(numbers), max(numbers)

def mean_median(*numbers):
	sorted_numbers = sorted(numbers)
	return sum(numbers)/len(numbers), numbers[len(numbers)//2]
	
def calc(first, second, *rest):
	return first * 100 + second * 10 + sum(rest)

def calc2(first, *rest, second):
	return first * 100 + second * 10 + sum(rest)
print(calc2(1,2,2,3,second=4))

def print_func(a, b, c):
	print(a, b, c)

def print_default(a, b=0, c=10):
	print(a, b, c)

min_value, max_value = min_max(1,2,3,4,5,6)

print(min_value, max_value)

mean_value, median_value = mean_median (1, 9, 4, 2, 6, 8, 19)
print(mean_value, median_value)

print(calc(1, 2, 3, 4))
#print(calc(1))
print_func(1,2,3)
print_func(b=1, a=2, c=3)
print_default(1)
print_default(1,2)
print_default(1,2,3)
