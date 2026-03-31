class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!= 1:
            # find the sum
            total = 0
            while n > 0: 
                rem = n % 10
                total += rem ** 2
                n //= 10
            # if we see numner we already saw return false 
            if total in seen:
                 return False 
            seen.add(total) 

            # make the num = n
            n = total 

        return True 