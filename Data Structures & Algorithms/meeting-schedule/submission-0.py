"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Easy solution in nlog(n)

        intervals.sort(key=lambda x : x.start)
        prev_end = None
        for inter in intervals:
            start, end = inter.start, inter.end
            if prev_end and prev_end > start:
                return False
            prev_end = end
        return True
