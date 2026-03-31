class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            sum_without_carry = a ^ b 
            carry = (a & b) << 1
            a = sum_without_carry 
            b = carry 
        
        return a & mask if b > mask else a 