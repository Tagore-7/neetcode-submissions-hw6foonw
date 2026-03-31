class Solution:
    def longestPalindrome(self, s: str) -> str:
        # think so if we have string ababd in a string last and first letter should be same 
        # so if we start taking last and first compare them if they equal we increment and we coninue so
        # until left and right cross 
        # but what happens if left and right are not equal 
        # should we keep left same and decrement the right? that would work? 
        # we do this middle so it's optimal
        res = "" # to store the longest palindrome 
        # how to find even or odd 
        res_len = 0

        for i in range(len(s)):
            # odd length 
            l, r = i,  i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l: r + 1]
                    res_len = r -  l + 1
                l -= 1 
                r += 1 

            # even length 
            l , r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l: r + 1]
                    res_len = r -  l + 1
                l -= 1 
                r += 1 

        return res

        

        