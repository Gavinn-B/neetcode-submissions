class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        int r = grid.length, c = grid[0].length;

        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(grid[i][j] == 1){
                    int count = bfs(grid,i,j);
                    if(count > res){
                        res = count;
                    }
                }
            }
        }
        return res;
    }

    private int bfs(int[][] grid, int r, int c){
        int[][] directions = {{1,0},{-1,0},{0,-1},{0,1}};
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r,c});
        int res = 1;
        grid[r][c] = 0;
        while(!q.isEmpty()){
            int[] node = q.poll();
            int row = node[0], col = node[1];
            
            for(int[] dir : directions){
                int nr = row + dir[0], nc = col + dir[1];
                if(nr >= 0 && nc >= 0 && nr < grid.length
                 && nc < grid[0].length && grid[nr][nc]==1){
                    q.add(new int[]{nr,nc});
                    grid[nr][nc] = 0;
                    res++;
                }
            }
        }
        return res;
    }

}
