class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        res = []
        for w in words:
            res.append(w[::-1])
        return " ".join(res)
        