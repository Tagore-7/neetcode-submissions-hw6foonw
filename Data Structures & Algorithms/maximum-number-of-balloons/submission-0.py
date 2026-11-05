class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        for ch in text:
            if ch in "ballon":
                count[ch] += 1

        if len(count) < 5:
            return 0

        count["l"] //= 2
        count["o"] //= 2

        return min(count.values())


        