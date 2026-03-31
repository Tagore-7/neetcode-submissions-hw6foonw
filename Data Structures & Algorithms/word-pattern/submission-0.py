class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False 

        cmap = {}
        wmap = {}

        for c, w in zip(pattern, words):
            if c in cmap and cmap[c] != w:
                return False 
            if w in wmap and wmap[w] != c:
                return False 

            cmap[c] = w
            wmap[w] = c

        return True 