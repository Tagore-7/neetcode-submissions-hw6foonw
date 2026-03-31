class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # O(n)
        # bitwise AND n and n - 1 
        if n < 0 or not n:
            return False 

        return n & (n - 1) == 0
        # if n < 0 or not n:
        #     return False 
    
        # while n > 1:
        #     if n % 2 == 0:
        #         n = n // 2
        #     else:
        #         return False 

        # return True if n == 1 else False
        