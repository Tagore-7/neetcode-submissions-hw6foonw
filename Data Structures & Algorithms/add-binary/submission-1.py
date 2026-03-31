class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        l, r = len(a) - 1, len(b) - 1
        carry = 0
        while l >= 0 or r >= 0 or carry:
            f1 = int(a[l]) if l >= 0 else 0
            f2 = int(b[r]) if r >= 0 else 0

            total = f1 + f2 + carry 
            last = total % 2
            carry = total // 2

            res.append(str(last))
            
            l-= 1
            r -= 1

        return "".join(res[::-1])

            


        