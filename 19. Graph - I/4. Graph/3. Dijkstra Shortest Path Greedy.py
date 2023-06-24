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

    def shortestDistDijkstra(self, src, n):
        dist = [float("inf")] * n
        st = set()
        # intiial steps
        dist[src] = 0
        st.add((0, src))

        while st:
            # fetch the smallest or first eklement from set
            nodeDistance, node = min(st)
            # pop from set
            st.remove((nodeDistance, node))

            # neighbour traverse
            for nbr, wt in self.adjList[node]:
                if nodeDistance + wt < dist[nbr]:
                    # mujhe distance update krna h 
					          # finding entry in set

                    # if found, then remove
                    if (dist[nbr], nbr) in st:
                        st.remove((dist[nbr], nbr))

                    # updation in dist array and set
                    dist[nbr] = nodeDistance + wt
                    st.add((dist[nbr], nbr))

        print("Printing Ans:")
        print(*dist, sep=", ")


if __name__ == "__main__":
    g = Graph()

    g.addEdge(6, 3, 2, 1)
    g.addEdge(6, 1, 14, 1)
    g.addEdge(3, 1, 9, 1)
    g.addEdge(3, 2, 10, 1)
    g.addEdge(1, 2, 7, 1)
    g.addEdge(2, 4, 15, 1)
    g.addEdge(4, 3, 11, 1)
    g.addEdge(6, 5, 9, 1)
    g.addEdge(4, 5, 6, 1)

    g.printAdjList()

    g.shortestDistDijkstra(6, 7)



