class Solution:
    def countElements(self, arr: List[int]) -> int:
        arrset = set(sorted(arr))
        count = 0

        for i in range(len(arr)):
            if arr[i] + 1 in arrset:
                count += 1


        return count 