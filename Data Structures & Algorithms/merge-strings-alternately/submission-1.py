class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointer approach 
        left, right = 0, 0
        res = []

        while left < len(word1) and right < len(word2):
            res.append(word1[left])
            res.append(word2[right])
            left += 1
            right += 1 

        while  left < len(word1):
            res.append(word1[left])
            left += 1

        while  right < len(word2):
            res.append(word2[right])
            right += 1

        return "".join(res)

            

