class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = defaultdict(int)
        unique = set()
        count = 0
        for ch in t:
            dict_t[ch] += 1
            count+=1
            unique.add(ch)
        
        left, right = 0, 0
        n = len(s)
        min_substring = ""
        while right<n or len(unique) == 0:
            if len(unique) == 0:
                # Substring has all characters so let's try reducing it
                if not min_substring or len(min_substring) > right-left:
                    min_substring = s[left:right]

                if s[left] in dict_t:
                    dict_t[s[left]] += 1
                    if dict_t[s[left]] == 1:
                        unique.add(s[left])
                    count+=1
                left+=1
                
            else:
                if s[right] in dict_t:
                    dict_t[s[right]] -= 1
                    if dict_t[s[right]] == 0:
                        unique.remove(s[right])
                    count -= 1
                right += 1
        
        return min_substring




        
        
        
