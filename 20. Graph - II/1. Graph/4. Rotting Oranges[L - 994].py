# https://leetcode.com/problems/rotting-oranges/

# CodeHelp

from typing import List
from queue import Queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = Queue()
        arr = [row[:] for row in grid]  # Create a deep copy of the grid
        count = 0
        ansTime = 0

        # Insert all rotten oranges in the queue
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    # Rotten orange found
                    coordinate = (row, col)
                    q.put((coordinate, 0))

        while not q.empty():
            fNode, time = q.get()
            x, y = fNode
            ansTime = max(ansTime, time)

            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]

                if (
                    0 <= newX < len(arr) and
                    0 <= newY < len(arr[0]) and
                    arr[newX][newY] == 1
                ):
                    newCoordinates = (newX, newY)
                    q.put((newCoordinates, time + 1))
                    # Mark orange as rotten 
                    arr[newX][newY] = 2

        # Check for any fresh orange
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 1:
                    return -1

        return ansTime
































# from collections import deque

# # Time complexity: O(rows * cols) -> each cell is visited at least once
# # Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
        
#         # number of rows
#         rows = len(grid)
#         if rows == 0:  # check if grid is empty
#             return -1
        
#         # number of columns
#         cols = len(grid[0])
        
#         # keep track of fresh oranges
#         fresh_cnt = 0
        
#         # queue with rotten oranges (for BFS)
#         rotten = deque()
        
#         # visit each cell in the grid
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 2:
#                     # add the rotten orange coordinates to the queue
#                     rotten.append((r, c))
#                 elif grid[r][c] == 1:
#                     # update fresh oranges count
#                     fresh_cnt += 1
        
#         # keep track of minutes passed.
#         minutes_passed = 0
        
#         # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
#         while rotten and fresh_cnt > 0:

#             # update the number of minutes passed
#             # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
#             minutes_passed += 1
            
#             # process rotten oranges on the current level
#             for _ in range(len(rotten)):
#                 x, y = rotten.popleft()
                
#                 # visit all the adjacent cells
#                 for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#                     # calculate the coordinates of the adjacent cell
#                     xx, yy = x + dx, y + dy
#                     # ignore the cell if it is out of the grid boundary
#                     if xx < 0 or xx == rows or yy < 0 or yy == cols:
#                         continue
#                     # ignore the cell if it is empty '0' or visited before '2'
#                     if grid[xx][yy] == 0 or grid[xx][yy] == 2:
#                         continue
                        
#                     # update the fresh oranges count
#                     fresh_cnt -= 1
                    
#                     # mark the current fresh orange as rotten
#                     grid[xx][yy] = 2
                    
#                     # add the current rotten to the queue
#                     rotten.append((xx, yy))

        
#         # return the number of minutes taken to make all the fresh oranges to be rotten
#         # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
#         return minutes_passed if fresh_cnt == 0 else -1