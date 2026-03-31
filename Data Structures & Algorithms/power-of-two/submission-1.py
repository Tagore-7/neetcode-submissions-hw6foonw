class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0 or not n:
            return False 
    
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                return False 

        return True if n == 1 else False
        