"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : x.start)

        room_stack = []
        room_count = 0
        for meeting in intervals:
            start, end = meeting.start, meeting.end
            if not room_stack or room_stack[0] > start:
                # Add a new room
                heapq.heappush(room_stack, end)
                room_count += 1
            else:
                # Remove finished meeting and add new meeting in the room
                heapq.heappop(room_stack)
                heapq.heappush(room_stack, end)
        
        return room_count







        return len(room_stack)


        