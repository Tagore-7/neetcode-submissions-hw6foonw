class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            sub_res = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j - 1] < nums[j]:
                    sub_res += nums[j]
                else:
                    break 
            res = max(res, sub_res)
        return res