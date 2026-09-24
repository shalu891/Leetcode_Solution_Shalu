class Solution(object):
    def findTheDifference(self, s, t):
        ch = 0
        for char in s:
            ch ^= ord(char)
        for char in t:
            ch ^= ord(char)
        return chr(ch)

        
        