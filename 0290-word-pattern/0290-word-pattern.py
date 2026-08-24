class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        return len(pattern) == len(words) and len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))
        