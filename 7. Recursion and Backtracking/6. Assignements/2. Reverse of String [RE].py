def reverse(s, start, end):
    # base case
    if start >= end:
        return

    # ek case
    s[start], s[end] = s[end], s[start]

    # baaki re khud smbhal lega
    reverse(s, start + 1, end - 1)

s = ['A', 'n', 's', 'h']
reverse(s, 0, len(s)-1)
print(''.join(s))
