class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        
        adj = {i: [] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visiting = set()
        discovered = 0

        def dfs(i, par):
            nonlocal discovered
            if i in visiting:
                return False
            discovered += 1
            visiting.add(i)
            
            for nei in adj[i]:
                if nei == par: continue
                else:
                    if not dfs(nei, i):
                        return False
            return True
        

        return dfs(0, -1) and (discovered == n)
            





        