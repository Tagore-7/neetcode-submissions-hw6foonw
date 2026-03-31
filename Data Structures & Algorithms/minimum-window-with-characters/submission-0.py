class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tmap = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            tmap[c] += 1

        have = 0
        need = len(tmap)
        res = [-1, -1]
        resLen = float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in tmap and window[c] == tmap[c]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                window[s[left]] -= 1

                if s[left] in tmap and window[s[left]] < tmap[s[left]]:
                    have -= 1
                
                left += 1

        left, right = res

        return s[left: right + 1] if resLen != float("infinity") else ""

        

        
                
        