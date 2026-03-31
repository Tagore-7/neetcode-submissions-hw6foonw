class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        perimeter = 0
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for i, j in DIRS:
                        nr , nc = r + i, c + j 
                        if not (0 <= nr < ROWS and 0 <= nc < COLS):
                            perimeter += 1
                        
                        elif grid[nr][nc] == 0:
                            perimeter += 1

        return perimeter
