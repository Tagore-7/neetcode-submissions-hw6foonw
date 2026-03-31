class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # or operation of two numbers result in zero
        res = 0

        for n in nums:
            res ^= n 

        return res