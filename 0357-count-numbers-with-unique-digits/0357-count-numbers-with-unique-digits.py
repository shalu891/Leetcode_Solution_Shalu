class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        
        total = 10
        unique_digits = 9
        available_number = 9
        
        while n > 1 and available_number > 0:
            unique_digits = unique_digits * available_number
            total += unique_digits
            available_number -= 1
            n -= 1
            
        return total
        