class Solution:
    def removeVowels(self, s: str) -> str:
        res = [] 

        for c in s:
            if c in ('a', 'e','i','o','u'):
                continue
            else:
                res.append(c)

        return "".join(res)

