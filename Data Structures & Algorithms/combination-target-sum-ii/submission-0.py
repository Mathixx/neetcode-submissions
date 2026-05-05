class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(currVal, i, comb):
            if currVal == 0:
                result.append(comb[::])
                return
            if i == len(candidates): return
            
            cand = candidates[i]
            currVal += cand
            if currVal > 0: return
            comb.append(cand)
            backtrack(currVal, i+1, comb)
            currVal -= cand
            comb.pop()

            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+=1
            backtrack(currVal, i+1, comb)
        
        backtrack(-target, 0, [])
        return result
        