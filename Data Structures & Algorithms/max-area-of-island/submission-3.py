class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visit = set()
        DIRS = [(0 , 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                r, c = q.popleft()
                for i, j in DIRS:
                    nr, nc = r + i, c + j
                    if (nr in range(ROWS) and 
                       nc in range(COLS) and 
                       grid[nr][nc] == 1 and 
                       (nr, nc) not in visit):
                       area += 1
                       q.append((nr, nc))
                       visit.add((nr, nc))
            return area 


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    newArea =  bfs(r, c)
                    maxArea = max(maxArea , newArea)
        return maxArea