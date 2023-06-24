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

    def shortestPathBfs(self, src, dest):
        queue = deque()
        visited = defaultdict(bool)
        parent = defaultdict(int)

        # inital steps for src
        queue.append(src)
        visited[src] = True
        parent[src] = -1

        while queue:
            fNode = queue.popleft()

            for nbr, _ in self.adjList[fNode]:
                if not visited[nbr]:
                    queue.append(nbr)
                    visited[nbr] = True
                    parent[nbr] = fNode
        # store path in ans, after traversing in the parent array
        ans = []
        node = dest
        while node != -1:
            ans.append(node)
            node = parent[node]

        ans.reverse()

        print("Printing Ans:")
        print(*ans, sep=", ")

if __name__ == "__main__":
    g = Graph()

    g.addEdge(0, 1, 1, 1)
    g.addEdge(1, 2, 1, 1)
    g.addEdge(2, 3, 1, 1)

    g.addEdge(3, 4, 1, 1)
    g.addEdge(0, 5, 1, 1)
    g.addEdge(5, 4, 1, 1)

    g.addEdge(0, 6, 1, 1)
    g.addEdge(6, 7, 1, 1)
    g.addEdge(8, 6, 1, 1)
    g.addEdge(8, 4, 1, 1)

    g.printAdjList()

    src = 0
    dest = 4
    g.shortestPathBfs(src, dest)
