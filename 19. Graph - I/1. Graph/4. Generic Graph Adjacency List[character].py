from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

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
        for node in self.adjList:
            print(node, "->", end=" ")
            for neighbour in self.adjList[node]:
                print(neighbour, end=", ")
            print()

if __name__ == "__main__":
    g = Graph()
    g.addEdge('a', 'b', 0)
    g.addEdge('b', 'c', 0)
    g.addEdge('a', 'c', 0)
    g.printAdjacencyList()
