class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # include and not inlcude dynamic programming  
        res = nums[0]
        curMax = curMin = 1

        for num in nums:
            oldMax = curMax 
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, oldMax * num, curMin * num)
            res = max(res, curMax)

        return res
        