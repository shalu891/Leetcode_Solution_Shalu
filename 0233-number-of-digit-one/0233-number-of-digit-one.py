class Solution(object):
    def countDigitOne(self, n):
        if n <= 0:
            return 0

        count = 0 
        i = 1
        while i <= n:
            divider = i * 10
            count += (n // divider) * i
            count += max(0, min(n % divider - i +1, i))
            i *= 10

        return count

        
        