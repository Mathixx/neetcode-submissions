class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort()

        curr = [0, 0, 0]
        for triplet in triplets:
            a,b,c = triplet[0], triplet[1], triplet[2]
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            else:
                curr[0] = max(curr[0], a)
                curr[1] = max(curr[1], b)
                curr[2] = max(curr[2], c)
                if curr == target:
                    return True
        return False
            
