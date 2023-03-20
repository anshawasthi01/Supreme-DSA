# Interger Variable always pass by value in python

def checkKey(name, i, n, key, count):
        # base case
        if(i >= n):
            # key not found
            print(count)
            return

        # 1 case solve krdo
        if(name[i] == key):
            # store in vector
            ans.append(i)
            count += 1
        
        # baaki recursion sambhal lega
        checkKey(name, i+1, n, key, count)

name = "lovebabbar"
n = len(name)

key = 'b'
i = 0
ans = []
count = 0
checkKey(name,i, n, key, count);
# print(count, end = ' ')

print("printing ans")
for val in ans:
    print(val, " ", end = ' ') 

