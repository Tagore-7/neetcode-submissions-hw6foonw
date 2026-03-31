class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        i = 0
        while i < len(s):
            ch = s[i]

            if ch == "(":
                low += 1
                high += 1

            elif ch == ")":
                low -= 1
                high -= 1

            else:
                low = low - 1
                high = high + 1

            if high < 0:
                return False 

            if low < 0:
                low = 0 

            i  += 1

        return low == 0
