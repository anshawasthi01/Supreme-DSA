def factorial(n):
	# base case
	if(n == 1):
		return 1

	chotiProblemAns = factorial(n-1)
	badiProblemAns = n * chotiProblemAns

	return badiProblemAns

n = int(input())
print("Enter the value of n  ")
ans  = factorial(n);
print("Answer is: ",ans, end=' ')


