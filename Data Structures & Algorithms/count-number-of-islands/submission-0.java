class Solution {
    public int numIslands(char[][] grid) {
        int r = grid.length, c = grid[0].length;
        int islands = 0;

        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(grid[i][j] == '1'){
                    bfs(grid, i, j);
                    islands++;
                }
            }
        }

        return islands;
    }
    private void bfs(char[][] grid, int i, int j){
        Queue<int[]> q = new LinkedList<>();
        int[][] directions = {{1,0},{-1,0},{0,-1},{0,1}};
        // track visited
        grid[i][j] = '0';
        // add to queue
        q.add(new int[]{i,j});

        while(!q.isEmpty()){
            // dequeue
            int[] node = q.poll();
            int row = node[0], col = node[1];

            for(int[] dir: directions){
                int nr = row + dir[0], nc = col + dir[1]; 
                if(nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length
                    && grid[nr][nc]=='1'){
                        q.add(new int[]{nr,nc});
                        grid[nr][nc] = '0';
                    }
            }
            
        }

    }
}
