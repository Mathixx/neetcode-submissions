import numpy as np

class Solution:
    def __init__(self):
        # This runs when you call Solution()
        # Every instance now has its own unique separator
        self.random_separator = str(np.random.rand())

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "EMPTY"
        return self.random_separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY": return []
        return s.split(self.random_separator)
