class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        nmap = defaultdict(int)

        for num in nums:
            count += nmap[num]
            nmap[num] += 1

        return count

