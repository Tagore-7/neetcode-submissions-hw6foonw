class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return nums 
        if len(nums) == 1:
            return nums[-1]
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            curSum = max(curSum , 0)
            curSum += num
            maxSum = max(maxSum, curSum)
            
            
            
            
        return maxSum
