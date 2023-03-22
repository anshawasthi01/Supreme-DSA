def print_permutation(str, i):
    # base case
    if i >= len(str):
        print(str, end=' ')
        return

    # swapping
    for j in range(i, len(str)):
        # swap
        str_list = list(str)
        str_list[i], str_list[j] = str_list[j], str_list[i]
        str = ''.join(str_list)

        # recursive call
        print_permutation(str, i + 1)

        # // backtracking, why?
        str_list = list(str)
        str_list[i], str_list[j] = str_list[j], str_list[i]
        str = ''.join(str_list)

# test the implementation
str = "abc"
print_permutation(str, 0)