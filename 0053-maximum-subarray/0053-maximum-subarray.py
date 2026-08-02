class Solution(object):
    def maxSubArray(self, nums):
        maxi = float("-inf")
        total = 0

        for _ in range(0, len(nums)):
            total += nums[_]
            maxi = max(maxi, total)
            
            if total < 0:
                total = 0

        return maxi
        

    