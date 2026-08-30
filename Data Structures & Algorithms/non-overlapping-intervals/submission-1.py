class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        count = 0
        intervals.sort()
        while i<len(intervals):
            if i<len(intervals)-1 and intervals[i][1]>intervals[i+1][0]:
                if intervals[i][1]>intervals[i+1][1]:
                    intervals[i] = intervals[i+1]
                else:
                    intervals[i+1] = intervals[i]
                count+=1
            i+=1

        return count
