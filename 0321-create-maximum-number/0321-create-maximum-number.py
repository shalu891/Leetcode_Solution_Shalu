class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def maxArray(nums, count):
            stack = []
            drop = len(nums) - count
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:count]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in range(len(a) + len(b))]

        m, n = len(nums1), len(nums2)
        res = []
        
        for i in range(max(0, k - n), min(k, m) + 1):
            res = max(res, merge(maxArray(nums1, i), maxArray(nums2, k - i)))
            
        return res
        

        

       
        