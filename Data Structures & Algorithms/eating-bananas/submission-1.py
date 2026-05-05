class Solution:
    def feasible(self, piles, h, k):
        count = 0
        for pile in piles:
            a, b = divmod(pile, k)
            count += a
            if b: count += 1
        return (count <= h)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h: return -1

        n = len(piles)
        maxpile = 0
        for pile in piles:
            maxpile = max(maxpile, pile)
        
        l, r = 1, maxpile
        while l < r:
            m = (l+r)//2
            if self.feasible(piles, h, m):
                r = m
            else:
                l = m + 1
        
        return l


        