class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, num in enumerate(nums):
            val = target - num
            if val in numMap:
                return [ numMap[val], i]
            numMap[num] = i 
                