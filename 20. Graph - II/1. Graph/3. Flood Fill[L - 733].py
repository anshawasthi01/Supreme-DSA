# https://leetcode.com/problems/flood-fill/description/

# CodeHelp 

from typing import List
from collections import deque

class Solution:
    def dfs(self, x, y, oldColor, newColor, vis, arr):
        vis[(x, y)] = True
        arr[x][y] = newColor

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if (
                0 <= newX < len(arr) and
                0 <= newY < len(arr[0]) and
                (newX, newY) not in vis and
                arr[newX][newY] == oldColor
            ):
                self.dfs(newX, newY, oldColor, newColor, vis, arr)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        vis = {}
        ans = [row[:] for row in image]  # Create a deep copy of the image

        self.dfs(sr, sc, oldColor, newColor, vis, ans)
        return ans












# class Solution(object):
#     def floodFill(self, image, sr, sc, newColor):
#         m, n = len(image), len(image[0])
#         color =  image[sr][sc]
#         if color == newColor:
#             return image
    
#         def dfs(sr, sc):
#             if image[sr][sc] == color:
#                 image[sr][sc] = newColor
                
#                 if sr >= 1: 
#                     dfs(sr-1, sc)
                    
#                 if sr+1 < m: 
#                     dfs(sr+1, sc)
                    
#                 if sc >= 1: 
#                     dfs(sr, sc-1)
                    
#                 if sc+1 < n: 
#                     dfs(sr, sc+1)

#         dfs(sr, sc)
#         return image
    
'''    
    
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        h, w = len(image), len(image[0])
        
		
        def dfs( r, c, src_color):
            
            if r < 0 or c < 0 or r >= h or c >= w or image[r][c] == newColor or image[r][c] != src_color:
                # Reject for invalid coordination, repeated traversal, or different color
                return
            
            # update color
            image[r][c] = newColor
            
            
            # DFS to 4-connected neighbors
            dfs( r-1, c, src_color )
            dfs( r+1, c, src_color )
            dfs( r, c-1, src_color )
            dfs( r, c+1, src_color )
            
        # ---------------------------------------------------------------------------
        
        dfs(sr, sc, src_color = image[sr][sc] )
        
        return image    
        
'''        