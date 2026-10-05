class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        count = Counter(s1.split() + s2.split())
        return [word for word, freq in count.items() if freq == 1]
        
        