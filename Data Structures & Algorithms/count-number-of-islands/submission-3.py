class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    self.dfs(grid, i, j)
                    islands+=1

        return islands

    def dfs(self, grid, i, j):
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        stack = []
        grid[i][j] = '0'
        stack.append((i, j))

        while len(stack) != 0:
            row, col = stack.pop()
            for dr,dc in directions:
                nr, nc = dr + row, dc + col
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == '0':
                    continue
                stack.append((nr,nc))
                grid[nr][nc] = '0'

