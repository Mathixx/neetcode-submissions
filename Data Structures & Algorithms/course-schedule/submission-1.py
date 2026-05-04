from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0]*numCourses

        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        visited = set()

        while q:
            a = q.popleft()
            if a in visited:
                return False

            visited.add(a)
            
            for nei in adj[a]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return (len(visited) == numCourses)
        


        