class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(nums) < 3:
            return -1

        sub = sorted(nums[:3])

        return sub[1]        