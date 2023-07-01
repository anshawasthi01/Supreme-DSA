# https://leetcode.com/problems/path-with-minimum-effort/

# CodeHelp
# dijkstra using Priority Queue

from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # < pair<int,pair<int,int> >, vector<pair<int,pair<int,int> > >, greater<pair<int,pair<int,int> > > >
        pq = [(0, 0, 0)]
        # dist(heights.size(), vector<int>(heights[0].size(), INT_MAX)
        dist = [[float('inf')] * len(heights[0]) for _ in range(len(heights))]
        dist[0][0] = 0

        while pq:
            frontNodeDifference, x, y = heappop(pq)

            # check ans tak toh nahi pahuch agye
            if x == len(heights) - 1 and y == len(heights[0]) - 1:
                return dist[x][y]

            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if 0 <= newX < len(heights) and 0 <= newY < len(heights[0]):
                    currDifference = abs(heights[x][y] - heights[newX][newY])
                    newMax = max(frontNodeDifference, currDifference)
                    if newMax < dist[newX][newY]:
                        dist[newX][newY] = newMax
                        heappush(pq, (newMax, newX, newY))

        return 0
