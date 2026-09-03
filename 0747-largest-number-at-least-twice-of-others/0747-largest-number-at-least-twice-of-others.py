class Solution(object):
    def dominantIndex(self, nums):
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        for x in nums:
            if x != max_val and max_val < 2 * x:
                return -1
                
        return max_idx
        
        