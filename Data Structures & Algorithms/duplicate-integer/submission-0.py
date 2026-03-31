class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}

        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                return True
        return False