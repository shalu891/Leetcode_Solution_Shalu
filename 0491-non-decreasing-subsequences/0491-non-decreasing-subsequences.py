class Solution(object):
    def findSubsequences(self, nums):
        result = set()
        
        def backtrack(index, current):
            if len(current) >= 2:
                result.add(tuple(current))
                
            for i in range(index, len(nums)):
                if not current or nums[i] >= current[-1]:
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()
                    
        backtrack(0, [])
        return list(result)


        