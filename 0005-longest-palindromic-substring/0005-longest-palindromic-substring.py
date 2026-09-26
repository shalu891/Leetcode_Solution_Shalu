class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) == 1:
            return s
        
        start = 0
        max_len = 0
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1, left + 1

        for i in range(len(s)):
            len1, start1 = expand_around_center(i, i)
            len2, start2 = expand_around_center(i, i + 1)
            
            if len1 > max_len:
                max_len = len1
                start = start1
            if len2 > max_len:
                max_len = len2
                start = start2
                
        return s[start:start + max_len]
    
        
        