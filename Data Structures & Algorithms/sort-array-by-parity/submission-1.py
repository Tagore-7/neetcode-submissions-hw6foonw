class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0

        for right in range(len(nums)):
            if not nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
        # odd, even = [], []

        # for num in nums:
        #     if num % 2:
        #         odd.append(num)
        #     else:
        #         even.append(num)
        # for num in odd:
        #     even.append(num)

        # return even

        