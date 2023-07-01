from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, wt, direction):
        # direction = 1 -> undirected graph
		    # direction => 0 -> directed graph
        self.adjList[u].append((v, wt))
        if direction:
            self.adjList[v].append((u, wt))

    def printAdjList(self):
        for i in self.adjList:
            print(i, "->", end=" ")
            for j in self.adjList[i]:
                print("(", j[0], ",", j[1], "),", end=" ")
            print()

    def floydWarshall(self, n):
        dist = [[float("inf")] * n for _ in range(n)]
        # diagnol pr zero mark krdo
        for i in range(n):
            dist[i][i] = 0

        # graph k according dist insert krdia h
        for u in self.adjList:
            for v, wt in self.adjList[u]:
                dist[u][v] = wt

        for helper in range(n):
            for src in range(n):
                for dest in range(n):
                    dist[src][dest] = min(dist[src][dest], dist[src][helper] + dist[helper][dest])

        print("Printing distance array:")
        for i in range(n):
            for j in range(n):
                print(dist[i][j], ",", end=" ")
            print()

g = Graph()

g.addEdge(0, 1, 3, False)
g.addEdge(0, 3, 5, False)
g.addEdge(1, 0, 2, False)
g.addEdge(1, 3, 4, False)
g.addEdge(2, 1, 1, False)
g.addEdge(3, 2, 2, False)

g.printAdjList()
g.floydWarshall(4)
