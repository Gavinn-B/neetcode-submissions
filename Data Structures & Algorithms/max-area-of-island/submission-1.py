class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]== 1:
                    area = self.bfs(grid, i, j)
                    if area > max_area:
                        max_area = area

        return max_area

    def bfs(self, grid, i, j):
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        q = deque()
        grid[i][j] = 0
        q.append((i, j))
        area = 1
        while len(q) != 0:
            row, col = q.popleft()
            for dr,dc in directions:
                nr, nc = dr + row, dc + col
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0:
                    continue
                q.append((nr,nc))
                grid[nr][nc] = 0
                area += 1
        return area

