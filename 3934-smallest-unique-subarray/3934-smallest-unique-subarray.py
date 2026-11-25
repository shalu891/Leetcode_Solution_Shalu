class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        base1 = 1315423911
        base2 = 2654435761

        def has_unique(length):
            if length == 0:
                return False
            
            h1 = 0
            h2 = 0
            p1 = pow(base1, length, mod1)
            p2 = pow(base2, length, mod2)
            
            counts = {}
            
            for i in range(n):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2
                
                if i >= length:
                    h1 = (h1 - nums[i - length] * p1) % mod1
                    h2 = (h2 - nums[i - length] * p2) % mod2
                
                if i >= length - 1:
                    pair = (h1, h2)
                    counts[pair] = counts.get(pair, 0) + 1
            
            for count in counts.values():
                if count == 1:
                    return True
            return False

        low = 1
        high = n
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
        