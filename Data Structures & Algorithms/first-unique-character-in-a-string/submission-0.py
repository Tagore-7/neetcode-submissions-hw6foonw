class Solution:
    def firstUniqChar(self, s: str) -> int:
        smap = {}

        for i,ch in enumerate(s):
            if ch in smap:
                smap[ch].append(i)
            else:
                smap[ch] = [i]
        print(smap)

        for key, val in smap.items():
            if len(val) == 1:
                return val[0]
        
        return -1
