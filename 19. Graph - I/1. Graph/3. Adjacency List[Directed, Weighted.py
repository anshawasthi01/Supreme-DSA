from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, weight, direction):
        # direction = 0 -> undirected graph
        # direction = 1 -> directed graph
        # create an edge from u to v with weight
        self.adjList[u].append((v, weight))
        if direction == 0:
            # undirected edge
            # create an edge from v to u with weight
            self.adjList[v].append((u, weight))

    def printAdjacencyList(self):
        for node in self.adjList:
            print(node, "->", end=" ")
            for neighbour, weight in self.adjList[node]:
                print(f"({neighbour},{weight})", end=", ")
            print()

if __name__ == "__main__":
    g = Graph()

    # directed input
    # g.addEdge(srcNode, destNode, weight, direction)
    g.addEdge(0, 1, 5, 1)
    g.addEdge(1, 2, 8, 1)
    g.addEdge(0, 2, 6, 1)
    print()
    g.printAdjacencyList()
