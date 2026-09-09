class Solution(object):
    def runningSum(self, nums):
        runningSum = []
        curr_total = 0

        for i in range(len(nums)):
            curr_total += nums[i]
            runningSum.append(curr_total)

        return runningSum

        