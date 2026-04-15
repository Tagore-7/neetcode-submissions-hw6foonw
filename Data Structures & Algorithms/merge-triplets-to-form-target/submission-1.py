class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # i think the better way is to check if target numbers
        # exist in the triplets in the same positions 
        good_ind = set()
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue 
            
            if a == target[0]:
                good_ind.add(0)
            if b == target[1]:
                good_ind.add(1)
            if c == target[2]:
                good_ind.add(2)

        return len(good_ind) == 3
            
        