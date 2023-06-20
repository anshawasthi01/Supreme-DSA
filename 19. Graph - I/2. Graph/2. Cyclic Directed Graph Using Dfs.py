from collections import defaultdict

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

    def checkCyclicDirectedGraphUsingDfs(self, src, visited, dfsVisited):
        visited[src] = True
        dfsVisited[src] = True

        for nbr in self.adjList[src]:
            if not visited[nbr]:
                aageKaAnswer = self.checkCyclicDirectedGraphUsingDfs(nbr, visited, dfsVisited)
                if aageKaAnswer:
                    return True
            if visited[nbr] and dfsVisited[nbr]:
                return True

        # yaha hi galti hoti h 
        dfsVisited[src] = False
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

ans = False
visited = defaultdict(bool)
dfsVisited = defaultdict(bool)
for i in range(n):
    if not visited[i]:
        ans = g.checkCyclicDirectedGraphUsingDfs(i, visited, dfsVisited)
        if ans:
            break

if ans:
    print("Cycle is Present")
else:
    print("Cycle Absent")
