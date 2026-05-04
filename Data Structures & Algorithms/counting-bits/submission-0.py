class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        log2n = 0
        while n >> log2n:
            log2n+=1
        
        i = 1
        res = [0, 1]
        while i < log2n+1:
            res_p_1 = [1 + cnt for cnt in res]
            res = res + res_p_1
            i += 1
        
        return res[:n+1]

        