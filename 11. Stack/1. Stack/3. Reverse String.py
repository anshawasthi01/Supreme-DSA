str = "babbar"

s = []
for c in str:
    s.append(c)

while s:
    print(s[-1], end=" ")
    s.pop()

print()