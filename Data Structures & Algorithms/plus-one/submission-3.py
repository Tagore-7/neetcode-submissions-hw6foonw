class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        res = str(int("".join(digits))  + 1 )
        q = []
        for ch in res:
            q.append(int(ch))


        return q