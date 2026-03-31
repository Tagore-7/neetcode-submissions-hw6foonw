class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = defaultdict(int)
        tmap = defaultdict(int)

        for s1, t1 in zip(s, t):
            # first time we see not there so add it
            if smap[s1]:
                if smap[s1] != t1:
                    return False 
            else:
                smap[s1] = t1 

            if tmap[t1]:
                if tmap[t1] != s1:
                    return False
            else:
                tmap[t1] = s1

        return True 