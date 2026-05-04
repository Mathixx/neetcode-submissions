class Solution:
    def isPalindrome(self, s:str) -> bool:
        if s and len(s) > 0 and s == s[::-1]:
            return True
        return False

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        res = []

        curr = []
        def backtrack(s, curr):
            if not s or len(s) == 0:
                res.append(curr.copy())
                return
            else:
                for i in range(len(s)+1):
                    if self.isPalindrome(s[:i]):
                        curr.append(s[:i])
                        backtrack(s[i:], curr)
                        curr.pop()
        
        backtrack(s, [])
        return res


        