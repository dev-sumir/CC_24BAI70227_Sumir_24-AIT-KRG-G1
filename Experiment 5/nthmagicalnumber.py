import math

class Solution:
    def nthMagicalNumber(self, n, a, b):
        MOD = 10**9 + 7
        
        lcm = (a * b) // math.gcd(a, b)
        
        low, high = min(a, b), n * min(a, b)
        
        while low < high:
            mid = (low + high) // 2
            
            count = mid // a + mid // b - mid // lcm
            
            if count >= n:
                high = mid
            else:
                low = mid + 1
        
        return low % MOD
