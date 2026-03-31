class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[-1, 0], [0, 1],  [1, 0],  [0, -1]]
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for i, j in DIRS:
                    nr, nc = r + i, c + j 
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue 
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
        
        