class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        # can add first value to res
        res = [intervals[0]]
        # iterate through everything but first value
        for s, e in intervals[1:]:
            # if the start is less than the last existing end in res
            if s <= res[-1][1]:
                # new end becomes max of last existing end and current end
                res[-1][1] = max(res[-1][1], e)
            else:
                # if no overlap, add current interval
                res.append([s, e])
        return res