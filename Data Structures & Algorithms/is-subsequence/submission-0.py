class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointers 
        left, right = 0, 0 

        # one point at s[0] and one point at t[0] 
        #now we check until if s[0] == t[0] 
        # if it does we increment left ++ 
        # if we don't anything then return false 
        # if we reached end in s then return true 

        while left != len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
         
            right += 1

        return left == len(s)
