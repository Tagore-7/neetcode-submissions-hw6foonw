class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        smap = set()
        for right in range(len(s)):
            while s[right] in smap:
                smap.remove(s[left])
                left += 1
            smap.add(s[right])
            length = max(length, right - left + 1)
        return length