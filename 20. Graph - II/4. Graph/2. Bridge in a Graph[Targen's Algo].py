from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, direction=True):
        # direction = True -> undirected graph
        # direction = False -> directed graph
        self.adjList[u].append(v)
        if direction:
            self.adjList[v].append(u)

    def findBridges(self, src, parent, timer, tin, low, vis):
        vis[src] = True
        tin[src] = timer
        low[src] = timer
        timer += 1

        for nbr in self.adjList[src]:
            if nbr == parent:
                continue
            # if not vis[nbr]:                         # list but In cpp same used in map
            if nbr not in vis or not vis[nbr]:         # map
                # dfs call
                self.findBridges(nbr, src, timer, tin, low, vis)
                # low update
                low[src] = min(low[src], low[nbr])
                # check for bridge
                if low[nbr] > low[src]:
                    print("{}--{} is a bridge".format(nbr, src))
            else:
                # node is visited and not a parent
                # low update
                low[src] = min(low[src], low[nbr])

# Create a graph object
g = Graph()

# Add edges to the graph
g.addEdge(0, 1, True)
g.addEdge(1, 2, True)
g.addEdge(2, 0, True)
g.addEdge(1, 6, True)
g.addEdge(3, 1, True)
g.addEdge(1, 4, True)
g.addEdge(3, 5, True)
g.addEdge(4, 5, True)

n = 7
timer = 0
# tin : Insertion Time
tin = [0] * n
low = [0] * n
# <int,bool>
vis = {}
g.findBridges(0, -1, timer, tin, low, vis)
