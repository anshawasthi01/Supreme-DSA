def fib(n):
	# base case
	if(n == 1):
		# first term 
		return 0

	if(n == 2):
		# second term
		return 1


	# RR -> f(n) = f(n-1) + f(n-2)
	ans = fib(n-1) + fib(n-2)
	return ans


n = int(input())
print("Enter the term you want to see")
ans  = fib(n);
print(n, "th term is: ",ans, end=' ')
