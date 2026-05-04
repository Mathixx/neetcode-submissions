class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l, r = i, i

            # even counts
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l-=1
                r += 1

            # Odd counts
            l, r = i, i+1

            # even counts
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l-=1
                r += 1
        
        return count

        