import fractions

class Solution(object):
    def maxLength(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                p *= nums[j]
                g = fractions.gcd(g, nums[j])
                l = (l * nums[j]) // fractions.gcd(l, nums[j])
                if p == l * g:
                    ans = max(ans, j - i + 1)
                if p > 2520 * l * g:
                    break
        return ans
        n = len(nums)
        ans = 0
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                p *= nums[j]
                g = math.gcd(g, nums[j])
                l = (l * nums[j]) // math.gcd(l, nums[j])
                if p == l * g:
                    ans = max(ans, j - i + 1)
                if p > 2520 * l * g:
                    break
        return ans