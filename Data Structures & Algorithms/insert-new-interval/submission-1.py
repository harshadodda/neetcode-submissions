class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        mergeInt = []
        for i in range(len(intervals)):
            # new interval is after current interval, could still overlap later
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # new interval is before current interval, cant overlap anymore
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # new interval is overlapping
            else:
                # make new interval from overlap, min of both starts and max of both ends
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        # at the end, add the new interval
        res.append(newInterval)
        return res
