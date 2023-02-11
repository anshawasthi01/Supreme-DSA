# N = 1 to N = 9
'''
#include <assert.h>
assert in cpp 
assert(n<=9)
'''
n = int(input())

for i in range(n):
    start_num_index = 8 - i 
    num = i + 1
    count_num = num

    for j in range(17):
        if j == start_num_index and count_num > 0:
            print(num,end='')
            start_num_index += 2
            count_num -= 1

        else:
            print("*",end='')

    print()