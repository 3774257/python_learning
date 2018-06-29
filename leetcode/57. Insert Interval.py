# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        rets = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i].end < newInterval.start:
            rets.append(intervals[i])
            i += 1
        start, end = newInterval.start, newInterval.end
        if i < n and start <= intervals[i].end:
            start = min(intervals[i].start, start)
        while i < n and end >= intervals[i].start:
            end = max(intervals[i].end, end)
            i += 1
        rets.append(Interval(start, end))
        rets.extend(intervals[i:])

        return rets


if __name__ == '__main__':
    a = [Interval(1,5)]
    b = Interval(5,7)
    sl = Solution()
    rets = sl.insert(a, b)
    for ret in rets:
        print(ret.start, ret.end)