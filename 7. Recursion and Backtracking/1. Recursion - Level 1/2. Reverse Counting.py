def printCounting(n):
	# base case
	if(n == 0):
		return
	# processing
	print(n,end = ' ')

	# re4ciursive relation
	printCounting(n-1)

n = int(input())
print("Enter the value of n  ")
ans  = printCounting(n)

