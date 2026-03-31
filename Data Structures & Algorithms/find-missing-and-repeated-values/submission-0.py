class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nset = set()
        res = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] in nset:
                    res.append(grid[i][j])
                else:
                    nset.add(grid[i][j]) 

        for i in range(1, (n ** 2) + 1):
            if i not in nset:
                res.append(i)

        return res