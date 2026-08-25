class Solution(object):
    def firstUniqChar(self, s):
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        for idx, char in enumerate(s):
            if counts[char] == 1:
                return idx
                
        return -1
        
        