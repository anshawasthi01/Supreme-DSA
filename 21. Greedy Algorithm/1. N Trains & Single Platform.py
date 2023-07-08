def solve(n, arr, dept):
    # < pair<int, int> >
    data = [(arr[i], dept[i]) for i in range(n)]
    data.sort(key=lambda x: x[1])
    
    cnt = 1
    print(data[0][0], "," ,data[0][1])
    last_dept = data[0][1]
    
    for i in range(1, n):
        if data[i][0] >= last_dept:
            # current train can be included
            cnt += 1
            last_dept = data[i][1]
            print(data[i][0], ",",data[i][1])
    
    return cnt


n = 4
arr = [5, 8, 2, 4]
dept = [7, 11, 6, 5]

ans = solve(n, arr, dept)
print("Answer is:",ans)

