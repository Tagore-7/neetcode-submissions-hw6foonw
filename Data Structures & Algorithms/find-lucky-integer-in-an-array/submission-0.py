class Solution:
    def findLucky(self, arr: List[int]) -> int:
        nmap = defaultdict(int)

        for n in arr:
            nmap[n] += 1

        res = -1
        for k, v in nmap.items():
            if k  == v:
                res = max(res, k)


        return res
        