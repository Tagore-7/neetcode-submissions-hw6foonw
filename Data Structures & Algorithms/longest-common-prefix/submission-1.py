class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        res = ""

        for i in range(len(first)):
            for w in strs:
                if i == len(w) or first[i] != w[i]:
                    return res 
            res += first[i]

        return res
                    