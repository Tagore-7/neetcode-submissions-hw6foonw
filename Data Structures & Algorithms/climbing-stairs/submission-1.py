class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dp(n , {})

    def dp(self, n: int, cache: dict) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = self.dp(n - 1, cache) +  self.dp(n - 2, cache)
        return cache[n]
