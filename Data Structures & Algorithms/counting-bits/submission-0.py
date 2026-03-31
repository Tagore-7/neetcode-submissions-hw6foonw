class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = []
        for i in range(n + 1):
            nums.append(self.count1bits(i))
        return nums

    def count1bits(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count