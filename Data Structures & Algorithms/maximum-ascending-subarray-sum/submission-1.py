class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]

            max_sum = max(max_sum, cur_sum)

        return max_sum
        # res = 0

        # for i in range(len(nums)):
        #     sub_res = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         if nums[j - 1] < nums[j]:
        #             sub_res += nums[j]
        #         else:
        #             break 
        #     res = max(res, sub_res)
        # return res