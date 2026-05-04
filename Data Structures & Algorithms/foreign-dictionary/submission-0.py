from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        characters = set([ch for word in words for ch in word])
        n_ch = len(characters)

        adj = {ch: set() for ch in characters}
        indegree = {ch: 0 for ch in characters}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        q = deque([ch for ch in indegree if indegree[ch]==0])
        res = ""
        while q:
            # Add q, remove indegree of its kids and it they hit 0 then add them to queue
            ch = q.popleft()
            res += ch

            for nei in adj[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                elif indegree[nei] < 0:
                    return ""

        return res if len(res) == len(characters) else ""
        



        