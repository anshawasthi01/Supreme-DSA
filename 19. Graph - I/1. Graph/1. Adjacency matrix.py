n = int(input("Enter the number of nodes: "))
adj = [[0] * n for _ in range(n)]

e = int(input("Enter the number of edges: "))
for _ in range(e):
    u, v = map(int, input().split())
    adj[u][v] = 1

# Printing adjacency matrix
for i in range(n):
    for j in range(n):
        print(adj[i][j], end=" ")
    print()




# Enter the number of nodes: 3
# Enter the number of edges: 6
# 0 1
# 1 0
# 1 2
# 2 1
# 0 2
# 2 0
# 0 1 1 
# 1 0 1 
# 1 1 0 