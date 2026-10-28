class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minv = str(min(nums))
        val = 0

        for ch in minv:
            val += int(ch)

        return 0 if val % 2 else 1