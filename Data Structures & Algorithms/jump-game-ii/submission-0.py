class Solution:
    def jump(self, nums: List[int]) -> int:
        far_can_go = 0
        current_jump_end = 0
        jumps = 0
        for i in range(len(nums) - 1):
            far_can_go = max(far_can_go, i + nums[i])
            if  i == current_jump_end:
                jumps += 1
                current_jump_end = far_can_go 

        return jumps