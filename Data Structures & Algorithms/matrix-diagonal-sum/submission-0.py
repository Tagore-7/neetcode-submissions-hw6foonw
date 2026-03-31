class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # primary diagnoal i == j 
        # what about secondary diagonal? 
        n = len(mat)
        res = 0
        i = 0

        while i < n:
            res +=  mat[i][i]
            res += mat[i][n - 1 - i]
            i += 1

        if n % 2:
            mid = n // 2
            res -= mat[mid][mid]

        return res 