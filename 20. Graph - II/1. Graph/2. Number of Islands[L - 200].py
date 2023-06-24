# https://leetcode.com/problems/number-of-islands/description/

#CodeHelp
from collections import deque

class Solution:
    def bfs(self, visited, row, col, grid):
        queue = deque()
        # initial steps
        queue.append((row, col))
        visited[(row, col)] = True

        while queue:
            x, y = queue.popleft()

            # i can move in 4 directions
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if (
                    0 <= new_x < len(grid) and
                    0 <= new_y < len(grid[0]) and
                    (new_x, new_y) not in visited and
                    grid[new_x][new_y] == '1'
                ):
                    queue.append((new_x, new_y))
                    visited[(new_x, new_y)] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        count = 0

        for row in range(len(grid)):
            n = len(grid[row])
            for col in range(n):
                if (row, col) not in visited and grid[row][col] == '1':
                    self.bfs(visited, row, col, grid)
                    count += 1

        return count
























        # def dfs(grid, i, j):
        #     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        #         return 
        #     grid[i][j] = '#'
        #     dfs(grid, i+1, j)
        #     dfs(grid, i-1, j)
        #     dfs(grid, i, j+1)
        #     dfs(grid, i, j-1)
        # count = 0
        # if not grid:
        #     return 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '1':
        #             dfs(grid, i, j)
        #             count += 1
                    
        # return count