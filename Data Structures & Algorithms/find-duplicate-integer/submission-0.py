class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cur = set()
        for num in nums:
            if num in cur:
                return num 
            cur.add(num)

        