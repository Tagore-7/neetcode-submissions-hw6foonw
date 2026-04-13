class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      LIS =  [1] * len(nums)
      #print(LIS)
      for i in range(len(nums) - 1, -1, -1): 
        # reverse order
        for j in range(i + 1, len(nums)):
            # reverse to len(nums) like 5 to 6 then 4 to 6 
            if nums[i] < nums[j]:
                # j = 6 i = 5
                LIS[i] = max(LIS[i], 1 + LIS[j]) # did not understand 
    
      return max(LIS)