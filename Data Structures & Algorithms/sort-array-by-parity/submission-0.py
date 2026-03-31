class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd, even = [], []

        for num in nums:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)
        for num in odd:
            even.append(num)

        return even

        