"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        prev_idx = float('-inf')
        intervals.sort(key=lambda x: x.start)
        
        for i in intervals:
            if prev_idx > i.start:
                return False
            prev_idx = i.end
        return True
