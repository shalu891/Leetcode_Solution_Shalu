class Solution(object):
    def lengthOfLastWord(self, s): 
        p = len(s) - 1

        while p >= 0 and s[p] == ' ':
            p -= 1

        length = 0
        while p >= 0 and s[p] != ' ':
            length += 1
            p -= 1

        return length

        
        