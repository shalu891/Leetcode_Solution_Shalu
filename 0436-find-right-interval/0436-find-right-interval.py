class Solution(object):
    def findRightInterval(self, intervals):
        n = len(intervals)
        starts = sorted((intervals[i][0], i) for i in range(n))
        start_values = [item[0] for item in starts]
        
        result = []
        for i in range(n):
            end_i = intervals[i][1]
            idx = bisect.bisect_left(start_values, end_i)
            
            if idx < n:
                result.append(starts[idx][1])
            else:
                result.append(-1)
                
        return result
       