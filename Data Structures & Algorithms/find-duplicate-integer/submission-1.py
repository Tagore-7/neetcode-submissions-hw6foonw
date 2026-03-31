class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # cur = set()
        # for num in nums:
        #     if num in cur:
        #         return num 
        #     cur.add(num)
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            

        