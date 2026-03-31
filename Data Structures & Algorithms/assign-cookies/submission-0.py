class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        left, right = 0, 0

        while left < len(g):
            while right < len(s)  and g[left] > s[right]:
                right += 1
            if right < len(s):
                left += 1
                right += 1
            else:
                break 
        
        return left 

        