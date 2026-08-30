class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        i = 0
        while i<len(intervals):
            if i<len(intervals)-1 and intervals[i][1] >= intervals[i+1][0]:
                min_val = min(intervals[i][0], intervals[i+1][0])    
                max_val = max(intervals[i][1], intervals[i+1][1])     
                intervals[i+1] = [min_val, max_val]
            else:
                res.append(intervals[i]) 
            i+=1    
              

        return res

        