class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        is_prime = bytearray([1]) * (n // 2)
        is_prime[0] = 0
        
        for i in range(1, int(n**0.5) // 2 + 1):
            if is_prime[i]:
                p = 2 * i + 1
                is_prime[p * p // 2 :: p] = bytearray((len(is_prime) - p * p // 2 - 1) // p + 1)
                
        return sum(is_prime) + 1
       
        