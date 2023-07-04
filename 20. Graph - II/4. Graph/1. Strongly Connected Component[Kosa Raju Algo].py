from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, direction):
        # direction = True -> undirected graph
        # direction = False -> directed graph
        self.adjList[u].append(v)
        if direction:
            self.adjList[v].append(u)

    def dfs1(self, src, s, vis):
        vis[src] = True

        for nbr in self.adjList[src]:                  
            # if not vis[nbr]:                         # list but In cpp same used in map
            if nbr not in vis or not vis[nbr]:         # map
                self.dfs1(nbr, s, vis)
        s.append(src)

    def dfs2(self, src, visited, adjNew):
        visited[src] = True
        print(src, end=", ")

        for nbr in adjNew[src]:
            # if not visited[nbr]:                      # list but In cpp same used in map
            if nbr not in visited or not visited[nbr]:  # map
                self.dfs2(nbr, visited, adjNew)

    def countSCC(self, n):
        s = []
        # unordered_map<int,bool>
        visited = {}

        # find topological ordering
        for i in range(n):
            if i not in visited:
                self.dfs1(i, s, visited)

        # reverse all edges
        # unordered_map<int,list<int> >
        adjNew = defaultdict(list)
        for u, nbrs in self.adjList.items():
            for v in nbrs:
                adjNew[v].append(u)

        # traverse using DFS
        count = 0
        visited2 = {}

        while s:
            node = s.pop()
            if node not in visited2:
                print("Printing {}th SCC:".format(count + 1), end=" ")
                self.dfs2(node, visited2, adjNew)
                print()
                count += 1

        return count

# Create a graph object
g = Graph()

# Add edges to the graph
g.addEdge(0, 1, False)
g.addEdge(1, 2, False)
g.addEdge(2, 3, False)
g.addEdge(3, 0, False)
g.addEdge(2, 4, False)
g.addEdge(4, 5, False)
g.addEdge(5, 6, False)
g.addEdge(6, 4, False)
g.addEdge(6, 7, False)

ans = g.countSCC(8)
print("Number of SCC:", ans)
