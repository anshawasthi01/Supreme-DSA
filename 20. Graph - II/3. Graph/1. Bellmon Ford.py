# relaxation : n-1 times
# n = nodes

from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, wt, direction):
        # direction = 1 -> undirected graph
		    # direction => 0 -> directed graph;
        self.adjList[u].append((v, wt))
        if direction:
            self.adjList[v].append((u, wt))

    def printAdjList(self):
        for i in self.adjList:
            print(i, "->", end=" ")
            for j in self.adjList[i]:
                print("(", j[0], ",", j[1], ")", end=" ")
            print()

    def bellmanFordAlgo(self, n, src):
        # assuming directed weightted graph
        dist = [float("inf")] * n
        dist[src] = 0

        # n-1 relaxation step
        for _ in range(n - 1):
            # for all edges
            for u in self.adjList:
                for v, wt in self.adjList[u]:
                    if dist[u] != float("inf") and dist[u] + wt < dist[v]:
                        dist[v] = dist[u] + wt

        # to check for -ve cycle
        negativeCycle = False
        for u in self.adjList:
            for v, wt in self.adjList[u]:
                if dist[u] != float("inf") and dist[u] + wt < dist[v]:
                    negativeCycle = True
                    break

        if negativeCycle:
            print("-ve cycle present")
        else:
            print("-ve cycle absent")

        print("Printing dist array:")
        for i in dist:
            print(i, end=" ")

g = Graph()

g.addEdge(0, 1, -1, False)
g.addEdge(0, 2, 4, False)
g.addEdge(1, 2, 3, False)
g.addEdge(1, 3, 2, False)
g.addEdge(1, 4, 2, False)
g.addEdge(3, 1, 1, False)
g.addEdge(3, 2, 5, False)
g.addEdge(4, 3, -3, False)

g.printAdjList()
g.bellmanFordAlgo(5, 0)
