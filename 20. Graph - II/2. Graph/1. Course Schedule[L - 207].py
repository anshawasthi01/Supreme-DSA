# https://leetcode.com/problems/course-schedule/description/

# CodeHelp
# TOPOLOGICAL SORT : Dependency  DAG

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
            # if(indegree[i] == 0):    in cpp
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
            # valid topo sort
            return True
        else:
            # invalid topo sort
            return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        # build adjacency list
        for task in prerequisites:
            u = task[0]
            v = task[1]
            if v in adjList:
                adjList[v].append(u)
            else:
                adjList[v] = [u]

        ans = self.topoSortBfs(numCourses, adjList)
        return ans
