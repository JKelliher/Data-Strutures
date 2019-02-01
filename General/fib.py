def fib(num):
	if num <=1:
		return(num)
	return(fib(num-2)+fib(num-1))


print(fib(4)) 