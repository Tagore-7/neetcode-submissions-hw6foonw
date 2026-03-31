class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for c in s:
            count[c] += 1 

        for i, c in enumerate(s):
            if count[c] == 1:
                return i 
        
        return -1
        # smap = {}

        # for i,ch in enumerate(s):
        #     if ch in smap:
        #         smap[ch].append(i)
        #     else:
        #         smap[ch] = [i]
        # # print(smap)

        # for key, val in smap.items():
        #     if len(val) == 1:
        #         return val[0]
        
        # return -1
