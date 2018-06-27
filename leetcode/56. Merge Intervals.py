"""https://leetcode.com/problems/merge-intervals/description/
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        if len(intervals) <= 1:
            return intervals
        rets = []
        start, end = intervals[0].start, intervals[0].end
        for val in intervals[1:]:
            if end >= val.start:
                end = max(end, val.end)
            else:
                rets.append(Interval(start, end))
                start, end = val.start, val.end
        rets.append(Interval(start, end))

        return rets
