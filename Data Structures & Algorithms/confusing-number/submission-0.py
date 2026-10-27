class Solution:
    def confusingNumber(self, n: int) -> bool:
        new = str(n)
        nd2 = "23457"
        newn = []

        for ch in new:
            if ch in nd2:
                return False 
            else:
                if ch == "6":
                    newn.append("9")
                elif ch == "9":
                    newn.append("6")
                else:
                    newn.append(ch)

        return int("".join(newn[::-1])) != n
        