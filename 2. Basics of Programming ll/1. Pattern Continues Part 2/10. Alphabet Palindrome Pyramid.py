n = int(input())

for r in range(1,n+1):
    for c in range(1, r +1):
        print(chr(c+65-1),end='')
		
	#reverse counting printing
    for c in range(r-1,0,-1):
        print(chr(c+65-1),end='')
    print()
