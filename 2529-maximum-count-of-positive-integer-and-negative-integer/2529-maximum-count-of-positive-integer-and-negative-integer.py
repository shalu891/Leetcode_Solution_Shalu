class Solution(object):
    def maximumCount(self, nums):
        n = len(nums)
        
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid
        neg = l
        
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid
        pos = n - l
        
        return max(neg, pos)