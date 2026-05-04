"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        
        heap = [] # One entry for each day and you only store the end
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            else:
                first_ending_time = heap[0]
                if first_ending_time <= interval.start:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
        
        return len(heap)

        