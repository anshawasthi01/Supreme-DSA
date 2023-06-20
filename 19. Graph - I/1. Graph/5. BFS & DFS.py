from collections import defaultdict, deque, OrderedDict

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

    def bfs(self, src, visited):
        q = deque()

        q.append(src)
        visited[src] = True

        while q:
            frontNode = q.popleft()
            print(frontNode, end=", ")

            # insert neighbours
            for neighbour in self.adjList[frontNode]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour] = True

    def dfs(self, src, visited):
        print(src, end=", ")
        visited[src] = True

        for neighbour in self.adjList[src]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited)

if __name__ == "__main__":
    g = Graph()
    # n -> number of nodes in graph
    n = 5
    g.addEdge(0, 1, 0)
    g.addEdge(1, 3, 0)
    g.addEdge(0, 2, 0)
    g.addEdge(2, 4, 0)

    g.printAdjacencyList()
    print()

    visited = OrderedDict((node, False) for node in g.adjList)
    # run a loop for all nodes
    print("Printing BFS Traversal:")
    for i in range(n):
        if not visited[i]:
            g.bfs(i, visited)
    print()

    visited2 = OrderedDict((node, False) for node in g.adjList)
    print("Printing DFS Traversal:")
    for i in range(n):
        if not visited2[i]:
            g.dfs(i, visited2)
    print()
