import collections

class Graph:
    def __init__(self):
        self.adjList = collections.defaultdict(list)

    def addEdge(self, u, v, direction):
        # direction = 0 -> undirected graph
        # direction = 1 -> directed graph
        # create an edge from u to v
        self.adjList[u].append(v)
        if direction == 0:
            # undirected edge
            # create an edge from v to u
            self.adjList[v].append(u)

    def printAdjacencyList(self):
        for node, neighbours in self.adjList.items():
            print(f"{node} -> ", end="")
            print(*neighbours, sep=", ")
            print()

    def topoSortDfs(self, src, visited, ans):
        visited[src] = True

        for neighbour in self.adjList[src]:
            if not visited[neighbour]:
                self.topoSortDfs(neighbour, visited, ans)

        # while returning, store the node in stack
        ans.append(src)

    def topoSortBfs(self, n):
        q = collections.deque()
        indegree = collections.defaultdict(int)

        # indegree calculation
        for src, neighbours in self.adjList.items():
            for nbr in neighbours:
                indegree[nbr] += 1

        # put all nodes inside queue, which has indegree=0
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        ans = []

        # bfs logic
        while q:
            fNode = q.popleft()

            ans.append(fNode)
            # or we can do count++ for Cycle detection using bfs

            for nbr in self.adjList[fNode]:
                indegree[nbr] -= 1
                # check for zero again # check for zero again
                if indegree[nbr] == 0:
                    q.append(nbr)
        return ans

# TOPOLOGICAL SORT Using DFS -> DFS traversal mein last m stack mein push kr lenge -> Roadmap Reallime example
g = Graph()
# n -> number of nodes in graph
n = 8
g.addEdge(0, 1, 1)
g.addEdge(1, 2, 1)
g.addEdge(2, 3, 1)
g.addEdge(3, 4, 1)
g.addEdge(3, 5, 1)
g.addEdge(4, 6, 1)
g.addEdge(5, 6, 1)
g.addEdge(6, 7, 1)

g.printAdjacencyList()
print()

visited = [False] * n
ans = []
for i in range(n):
    if not visited[i]:
      g.topoSortDfs(i, visited, ans)

print("Top Sort:")
while ans:
    print(ans.pop(), end=" ")
print()

# # must be DAG and Acyclic
# # TOPOLOGICAL SORT Using DFS OR Kahn's Algorithm
# g = Graph()
# # n -> number of nodes in graph
# n = 8
# g.addEdge(2, 4, 1)
# g.addEdge(2, 5, 1)
# g.addEdge(4, 6, 1)
# g.addEdge(5, 3, 1)
# g.addEdge(3, 7, 1)
# g.addEdge(6, 7, 1)
# g.addEdge(7, 0, 1)
# g.addEdge(7, 1, 1)

# g.printAdjacencyList()
# print()

# # connected or disconnected 
# ans = g.topoSortBfs(n)

# # # To find Cycle Detection Using BFS use below only if else code 
# # if len(ans) == n:
# #     print("It is a valid topo sort" )
# # else:
# #     print("Cycle Present or Invalid topo sort" )

# print("Printing Topological Sort using BFS:")
# print(*ans, sep=", ")



