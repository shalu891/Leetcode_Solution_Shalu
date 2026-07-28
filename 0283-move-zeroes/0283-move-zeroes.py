class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        temp = []

        for i in range(0, n):
            if nums[i] != 0:
                temp.append(nums[i])

        nZ = len(temp)
        for i in range(0, nZ):
            nums[i] = temp[i]

        for i in range(nZ, n):
            nums[i] = 0
       


