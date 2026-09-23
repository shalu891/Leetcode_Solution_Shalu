class Solution(object):
    def isPalindrome(self, s):
        filtered = [char.lower() for char in s if char.isalnum()]
        return filtered == filtered[::-1]
        
    
        