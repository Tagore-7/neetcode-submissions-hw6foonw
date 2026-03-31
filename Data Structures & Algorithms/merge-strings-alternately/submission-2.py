class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # more simple code 
        n = min(len(word1), len(word2))
        res = []
        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])

        res.append(word1[n:])
        res.append(word2[n:])

        return "".join(res)
        # # two pointer approach 
        # left, right = 0, 0
        # res = []

        # while left < len(word1) and right < len(word2):
        #     res.append(word1[left])
        #     res.append(word2[right])
        #     left += 1
        #     right += 1 

        # while  left < len(word1):
        #     res.append(word1[left])
        #     left += 1

        # while  right < len(word2):
        #     res.append(word2[right])
        #     right += 1

        # return "".join(res)

            

