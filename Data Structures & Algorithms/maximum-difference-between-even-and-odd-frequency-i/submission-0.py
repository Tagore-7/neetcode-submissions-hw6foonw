class Solution:
    def maxDifference(self, s: str) -> int:
        smap = defaultdict(int)

        for ch in s:
            smap[ch] += 1

        odd_freq = 0
        even_freq = float("inf")

        for key, val in smap.items():
            if val % 2:
                odd_freq = max(odd_freq, val)
            else:
                even_freq = min(even_freq, val)

        return odd_freq - even_freq

        