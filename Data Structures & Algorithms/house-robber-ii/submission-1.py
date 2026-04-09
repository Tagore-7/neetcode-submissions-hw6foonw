class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # maybe inluce and not inlcude? 
        def rob_linear(sub_nums):
            prev_max = 0
            curr_max = 0

            for amount in sub_nums:
                temp = curr_max
                curr_max = max(prev_max + amount, curr_max)
                prev_max = temp 

            return curr_max 


        range1 = nums[:-1]
        range2 = nums[1:]

        return max(rob_linear(range1), rob_linear(range2))

