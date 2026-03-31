class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS,COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visit = set()
        islands = 0
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            while queue:
                r, c = queue.popleft()
                for i, j in DIRS:
                    nr, nc = r + i, c + j
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1" and (nr, nc) not in visit:
                         queue.append((nr, nc))
                         visit.add((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
