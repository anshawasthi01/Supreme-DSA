# https://www.spoj.com/problems/DEFKIN/#:~:text=DEFKIN%20%2D%20Defense%20of%20a%20Kingdom&text=The%20tower%20defends%20all%20the,in%20the%20largest%20undefended%20rectangle.

x, y, n = map(int, input().split())
t = n
rowC = [0]
colC = [0]

for _ in range(t):
    a, b = map(int, input().split())
    rowC.append(a)
    colC.append(b)

# Size of 2D grid
rowC.append(x + 1)
colC.append(y + 1)

rowC.sort()
colC.sort()

maxLen = float('-inf')
for i in range(1, len(rowC)):
    a = rowC[i - 1]
    b = rowC[i]
    maxLen = max(maxLen, b - a - 1)

maxWidth = float('-inf')
for i in range(1, len(colC)):
    a = colC[i - 1]
    b = colC[i]
    maxWidth = max(maxWidth, b - a - 1)

print("Answer is", maxLen * maxWidth)
