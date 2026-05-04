class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        map_t = defaultdict(int)
        for ch in t:
            map_t[ch] += 1
        
        remaining_letters = len(map_t)
        left = 0
        right = 0
        min_string = None

        while right < len(s) or (remaining_letters == 0):
            if remaining_letters == 0:
                if not min_string or len(min_string) > right-left:
                    min_string = s[left:right]
                
                ch = s[left]
                if ch in map_t:
                    map_t[ch] += 1
                    if map_t[ch] == 1:
                        remaining_letters += 1 
                left += 1
            else:
                # adding letter right
                ch = s[right]
                if ch in map_t:
                    map_t[ch] -= 1
                    if map_t[ch] == 0:
                        remaining_letters -= 1
                right += 1
        
        return "" if not min_string else min_string
                