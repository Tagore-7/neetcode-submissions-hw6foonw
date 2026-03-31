class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = defaultdict(int)
        s2 = defaultdict(int)

        for c in ransomNote:
            s1[c] += 1

        for c in magazine:
            s2[c] += 1

        for key, val in s1.items():
            if s2[key]:
                if val > s2[key]:
                    return False 
            else:
                return False 
            
        return True 