class Solution(object):
    def reverseWords(self, s):
        left = 0 
        right = len(s) - 1

        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        res = []
        word = []

        while left <= right :
            if s[left] != ' ':
                word.append(s[left])
            elif word:
                res.insert(0, "".join(word))
                word =[] 
            left += 1

        if word:
            res.insert(0, "".join(word))

        return " ".join(res)      