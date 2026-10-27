class Solution(object):
    def lengthOfLIS(self, nums):
        sub = []
        for num in nums:
            idx = bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        
        return len(sub)
        
        