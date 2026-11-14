class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        
        curr_end = float('-inf')
        longest_chain = 0
        
        for left, right in pairs:
            if left > curr_end:
                longest_chain += 1
                curr_end = right
                
        return longest_chain
        