class Solution(object):
    def findMinDifference(self, timePoints):
        if len(timePoints) > 1440:
            return 0
        
        minutes = []
        for time in timePoints:
            hours, mins = map(int, time.split(':'))
            minutes.append(hours * 60 + mins)
            
        minutes.sort()
        
        min_diff = (1440 - minutes[-1]) + minutes[0]
        
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            if diff < min_diff:
                min_diff = diff
                
        return min_diff
        
        