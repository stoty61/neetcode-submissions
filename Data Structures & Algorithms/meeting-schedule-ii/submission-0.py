"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        rooms = 1

        timeline = [0] * max(interval.end for interval in intervals)

        for interval in intervals:
            for i in range(interval.start,interval.end):
                timeline[i] += 1

        return max(timeline)
