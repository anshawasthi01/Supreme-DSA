# https://leetcode.com/problems/course-schedule-ii/

# CodeHelp
# TOPOSORT : DAG

from collections import deque

class Solution:
    def topoSortBfs(self, n, adjList):
        ans = []
        q = deque()
        # <int, int>
        indegree = {}

        # Calculate indegree
        for i in adjList:
            src = i
            for nbr in adjList[i]:
                if nbr in indegree:
                    indegree[nbr] += 1
                else:
                    indegree[nbr] = 1

        # Put all nodes inside the queue, which have indegree=0
        for i in range(n):
            if i not in indegree:
                q.append(i)

        # BFS logic
        while q:
            fNode = q.popleft()

            ans.append(fNode)
            # or we can do count++

            if fNode in adjList:
                for nbr in adjList[fNode]:
                    indegree[nbr] -= 1
                    # Check for zero again
                    if indegree[nbr] == 0:
                        q.append(nbr)

        if len(ans) == n:
            # Valid topological sort
            return ans
        else:
            # Invalid
            return []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}

        # Build adjacency list
        for task in prerequisites:
            u = task[0]
            v = task[1]
            if v in adjList:
                adjList[v].append(u)
            else:
                adjList[v] = [u]

        ans = self.topoSortBfs(numCourses, adjList)
        return ans
