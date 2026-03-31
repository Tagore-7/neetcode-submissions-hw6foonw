class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for d in digits:
            res += str(d)

        num = int(res)
        num += 1 
        num = str(num)
        q = []
        for ch in num:
            q.append(int(ch))


        return q