from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, wt, direction):
      	# direction = 1 -> undirected graph
		    # direction => 0 -> directed graph
        self.adjList[u].append((v, wt))
        if direction == 1:
            self.adjList[v].append((u, wt))

    def printAdjList(self):
        for u, neighbors in self.adjList.items():
            print(u, "->", end=" ")
            for v, wt in neighbors:
                print("(", v, ",", wt, ")", end=" ")
            print()

    def topoSortDfs(self, src, visited, ans):
        visited[src] = True

        for neighbor, _ in self.adjList[src]:
            if not visited[neighbor]:
                self.topoSortDfs(neighbor, visited, ans)

        # while returning, store the node in stack
        print("Pushing", src)
        ans.append(src)

    def shortestpathDfs(self, dest, topoOrder, n):
        dist = [float("inf")] * n

        src = topoOrder[-1]
        topoOrder.pop()
        dist[src] = 0

        for nbr, wt in self.adjList[src]:
            if dist[src] + wt < dist[nbr]:
                dist[nbr] = dist[src] + wt

        while topoOrder:
            topElement = topoOrder[-1]
            topoOrder.pop()

            if dist[topElement] != float("inf"):
                for nbr, wt in self.adjList[topElement]:
                    if dist[topElement] + wt < dist[nbr]:
                        dist[nbr] = dist[topElement] + wt

        print("Printing Ans:")
        for i in range(n):
            print(i, "->", dist[i])

if __name__ == "__main__":
    g = Graph()

    g.addEdge(0, 1, 5, 0)
    g.addEdge(0, 2, 3, 0)
    g.addEdge(2, 1, 2, 0)

    g.addEdge(1, 3, 3, 0)
    g.addEdge(2, 3, 5, 0)
    g.addEdge(2, 4, 6, 0)

    g.addEdge(4, 3, 1, 0)


    g.printAdjList()

    topoOrder = []
    visited = defaultdict(bool)
    g.topoSortDfs(0, visited, topoOrder)

    g.shortestpathDfs(3, topoOrder, 5)
