def getSubsequences(string):
    ans = []
    n = len(string)

                    # 2 ki power n - 1
    for num in range(1 << n):
        temp = ""
        # we will create subsequence string in this temp string
        for i in range(n):
            ch = string[i]
            if num & (1 << i):
                # non-zero value k liye , include current character
                temp += ch

        if len(temp) >= 0:
            # store in ans
            ans.append(temp)

    ans.sort()
    print("Count of subsequences:", len(ans))
    print("Printing the subsequences:")
    for i in ans:
        print(i)

string = "abc"
getSubsequences(string)