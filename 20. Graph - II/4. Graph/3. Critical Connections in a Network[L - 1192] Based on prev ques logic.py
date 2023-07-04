# https://leetcode.com/problems/critical-connections-in-a-network/description/
# CodeHelp

# Targen's Algo : Starting and Finishing Time

from collections import defaultdict

class Solution:
    def findBridges(self, src, parent, timer, tin, low, vis, ans, adjList):
        vis[src] = True
        tin[src] = timer
        low[src] = timer
        timer += 1

        for nbr in adjList[src]:
            if nbr == parent:
                continue
            # if not vis[nbr]:                         # list but In cpp same used in map
            if nbr not in vis or not vis[nbr]:         # map
                # dfs call
                self.findBridges(nbr, src, timer, tin, low, vis, ans, adjList)
                # low update
                low[src] = min(low[src], low[nbr])
                # check for bridge
                if low[nbr] > tin[src]:
                    ans.append([nbr, src])
            else:
                # node is visited and not a parent
                # low update
                low[src] = min(low[src], low[nbr])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        adjList = defaultdict(list)

        for connection in connections:
            u = connection[0]
            v = connection[1]
            adjList[u].append(v)
            adjList[v].append(u)

        ans = []
        timer = 1
        tin = [0] * n
        low = [0] * n
        vis = {}
        self.findBridges(0, -1, timer, tin, low, vis, ans, adjList)

        return ans
