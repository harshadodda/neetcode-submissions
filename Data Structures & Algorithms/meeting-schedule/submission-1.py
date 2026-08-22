"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start) # sort by start times

        for i in range(1, len(intervals)): # start at second
            i1 = intervals[i - 1]
            i2 = intervals[i]

            # meeting 2 starts before meeting 1 ends 
            if i1.end > i2.start: 
                return False
        return True