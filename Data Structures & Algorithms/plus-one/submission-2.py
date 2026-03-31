class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        res = "".join(digits)

        num = int(res)
        num += 1 
        num = str(num)
        q = []
        for ch in num:
            q.append(int(ch))


        return q