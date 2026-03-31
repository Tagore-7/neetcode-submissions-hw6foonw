class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # two pointer appraoch 
        sset = defaultdict(int)

        for ch in s:
            sset[ch] += 1

        for ch in t:
            if not sset[ch]:
                return ch 
            sset[ch] -= 1 





        