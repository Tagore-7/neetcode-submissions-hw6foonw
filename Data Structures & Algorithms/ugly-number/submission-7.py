class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i 

        return n == 1

        # factor = 2

        # while n > 1:
        #     if n % factor == 0:
        #         if factor > 5 or factor == 4:
        #             return False 
        #         n /= factor 
        #     else:
        #         factor += 1



        # return True 