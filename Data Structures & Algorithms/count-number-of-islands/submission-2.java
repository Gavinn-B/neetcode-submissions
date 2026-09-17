class Solution {
    public int numIslands(char[][] grid) {
        int islands = 0;
        int r = grid.length;
        int c = grid[0].length;

        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(grid[i][j]=='1'){
                    bfs(grid,i,j);
                    islands++;
                }
            }
        }

        return islands;
    }

    public void bfs(char[][] grid, int r, int c){
        Queue<int[]> q = new LinkedList<>();
        grid[r][c] = '0';
        q.add(new int[]{r,c});
        int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};

        while(!q.isEmpty()){
            int[] node = q.poll();
            for(int[] dir : directions){
                int nr = node[0] + dir[0], nc = node[1] + dir[1];

                if(nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length
                    && grid[nr][nc]=='1'){
                        q.add(new int[]{nr,nc});
                        grid[nr][nc] = '0';
                    }
            }
        }
    }
}
