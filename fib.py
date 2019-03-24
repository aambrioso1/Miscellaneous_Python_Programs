def fib(n):
	if n==0:
		return 0
	if n==1:
		return 1
	total=fib(n-1)+fib(n-2)
	return total
print(fib(20))
