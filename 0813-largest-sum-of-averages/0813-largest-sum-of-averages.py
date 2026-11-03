class Solution(object):
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def average(i, j):
            return (prefix[j] - prefix[i]) / float(j - i)

        memo = {}

        def dp(i, k_groups):
            if k_groups == 1:
                return average(i, n)

            if (i, k_groups) in memo:
                return memo[(i, k_groups)]

            res = 0
            for j in range(i + 1, n - k_groups + 2):
                res = max(res, average(i, j) + dp(j, k_groups - 1))

            memo[(i, k_groups)] = res
            return res

        return dp(0, k)
        
        