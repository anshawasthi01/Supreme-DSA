# HW
n = int(input())

	# // for(int row=0; row<n; row = row + 1) {
	# // 	//spaces
	# // 	for(int col=0; col < n-row-1; col = col +1) {
	# // 		cout << " ";
	# // 	}

	# // 	//numerbers with spaces in between
	# // 	int start = 1;
	# // 	for(int col =0; col < 2*row+1; col = col + 1) {
	# // 		//first row or last row 
	# // 		if(row == 0 || row == n-1) {
	# // 			if(col %2 == 0) {
	# // 				//even
	# // 				cout << start;
	# // 				start = start + 1;
	# // 			}
	# // 			else {
	# // 				//odd
	# // 				cout << " ";
	# // 			}
	# // 		}
	# // 		else {
	# // 			//first col
	# // 			if(col == 0) {
	# // 				cout << 1;
	# // 			}
	# // 			else if(col == 2*row+1-1){
	# // 				cout << row+1;
	# // 			}
	# // 			else {
	# // 				cout <<" ";
	# // 			}
	# // 		}
	# // 	}
	# // 	cout << endl;
	# // }

for r in range(n):
    for c in range(n - r - 1): #spaces
        print(" ",end='')	

    for c in range(r + 1): #numbers
        print(r + c + 1,end='')

    start = 2*r
    for c in range(r): #reverse counting
        print(start,end='')
        start = start - 1

    print()


