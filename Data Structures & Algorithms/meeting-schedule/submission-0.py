"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # brute force 
        n = len(intervals)
        for i in range(n):
            firstMeet = intervals[i]
            for j in range(i + 1, n):
                secondMeet = intervals[j]
                if min(firstMeet.end, secondMeet.end) > max(firstMeet.start, secondMeet.start):
                    return False 

        return True 

        # sorting 
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            first = intervals[i - 1]
            second = intervals[i]

            if first.end > second.start:
                return False 

        return True 

