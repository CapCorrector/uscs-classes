import time
import sys

def fib(n):
	if n == 1 or n == 2:
		return n-1
	else:
		return fib(n-1) + fib(n-2)

def fib_memo(n):
	if n in memo:
		return memo[n]
	else:
		result = fib_memo(n-1) + fib_memo(n-2)
		memo[n] = result
		return result

memo = {1: 0, 2: 1}

#start = time.time()
#print(fib(30))
#end = time.time()
#print(end-start)

sys.setrecursionlimit(1000)
start = time.time()
print(fib_memo(10000))
end = time.time()
print(end-start)
