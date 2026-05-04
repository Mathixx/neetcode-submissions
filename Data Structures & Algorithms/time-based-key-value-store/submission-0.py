from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)
        # The value is gonna be a ordered list of tuples

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.time_dict[key], (timestamp, value), key=lambda x:x[0])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return ""
        else:
            idx = bisect.bisect_right(self.time_dict[key], timestamp, key=lambda x:x[0])
            if idx == 0:
                return ""
            else:
                return self.time_dict[key][idx-1][1]
        
