# CodeHelp

class Solution:
    def dfs(self, vis, src, isConnected):
        vis[src] = True
        # row -> src
        # col -> we will write a loop
        size = len(isConnected[src])
        for col in range(size):
            if src != col and isConnected[src][col] == 1:
                # col is a nbr
                if col not in vis or not vis[col]:  # map
                # if not vis[col]:                    #list but In cpp same used in map
                    self.dfs(vis, col, isConnected)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # <int, bool> map
        visited = {}

        # n = len(isConnected)
        # visited = [0] * n

        count = 0
        n = len(isConnected)
        # i represents nodes here
        for i in range(n):
            if i not in visited:   # map
            # if not visited[i]:       # list but In cpp same used in map
                self.dfs(visited, i, isConnected)
                count += 1
        return count



























        # # Devsnest
        # n = len(isConnected)
        # # Create a visited list to keep track of which cities have been visited
        # visited = [0] * n
        # # Initialize the number of provinces to 0
        # num_provinces = 0

        # for i in range(n):
        #     # If the city has not been visited yet
        #     if visited[i] == 0:
        #         # Use BFS to traverse all the cities that are directly or indirectly connected to it
        #         queue = deque([i])
        #         visited[i] = 1
        #         while queue:
        #             city = queue.popleft()
        #             for j in range(n):
        #                 if isConnected[city][j] == 1 and visited[j] == 0:
        #                     queue.append(j)
        #                     visited[j] = 1
        #         # Increase the number of provinces by 1
        #         num_provinces += 1
        # return num_provinces