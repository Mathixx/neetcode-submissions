class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        longest_substring = 0

        left, right = 0, 0
        while right < len(s):
            ch = s[right]
            if ch in last_seen:
                if last_seen[ch] >= left:
                    left = last_seen[ch] + 1
            last_seen[ch] = right
            longest_substring = max(longest_substring, right - left + 1)
            right += 1
        
        return longest_substring


        