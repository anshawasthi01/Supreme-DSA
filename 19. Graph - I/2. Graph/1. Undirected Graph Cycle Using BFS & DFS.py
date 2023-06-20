from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, direction):
        # direction = False -> undirected graph
        # direction = True -> directed graph
        # create an edge from u to v
        self.adjList[u].append(v)
        if not direction:
            # undirected edge
            # create an edge from v to u
            self.adjList[v].append(u)

    def printAdjacencyList(self):
        for node in self.adjList:
            print(node, "->", end=" ")
            for neighbour in self.adjList[node]:
                print(neighbour, end=", ")
            print()

    def checkCyclicUsingBfs(self, src, visited):
        q = deque()
        parent = {}
        
        q.append(src)
        visited[src] = True
        parent[src] = -1

        while q:
            frontNode = q.popleft()

            for nbr in self.adjList[frontNode]:
                if not visited[nbr]:
                    q.append(nbr)
                    visited[nbr] = True
                    parent[nbr] = frontNode
                if visited[nbr] and nbr != parent[frontNode]:
                    # cycle present
                    return True

        return False

    def checkCyclicUsingDfs(self, src, visited, parent):
        visited[src] = True

        for nbr in self.adjList[src]:
            if not visited[nbr]:
                checkAageKaAns = self.checkCyclicUsingDfs(nbr, visited, src)
                if checkAageKaAns:
                    return True
            if visited[nbr] and nbr != parent:
                # cycle present
                return True

        return False

g = Graph()
n = 5  # number of nodes in the graph
g.addEdge(0, 1, True)
g.addEdge(1, 2, True)
g.addEdge(2, 3, True)
g.addEdge(3, 4, True)
g.addEdge(4, 0, True)

g.printAdjacencyList()
print()

# # BFS Approach
# ans = False
# visited = defaultdict(bool)
# for i in range(n):
#     if not visited[i]:
#         ans = g.checkCyclicUsingBfs(i, visited)
#         if ans:
#             break

# if ans:
#     print("Cycle is Present")
# else:
#     print("Cycle Absent")

# DFS Approach
ansDfs = False
visitedDfs = defaultdict(bool)
for i in range(n):
    if not visitedDfs[i]:
        ansDfs = g.checkCyclicUsingDfs(i, visitedDfs, -1)
        if ansDfs:
            break

if ansDfs:
    print("Cycle is Present")
else:
    print("Cycle Absent")
