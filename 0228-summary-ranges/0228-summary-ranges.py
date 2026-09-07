class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1 

            end = nums[i]

            if start == end:
                ranges.append(str(start))
            else:
                ranges.append("{}->{}".format(start,end))

            i += 1

        return ranges
        