// Submission for Wedsnesday
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[][] mem = new int[m][n];
        return findAllPath(0, 0, m, n, mem, obstacleGrid);
    }
    
    public int findAllPath(int x, int y, int m, int n, int[][] mem, int[][] obstacleGrid) {
        if(x >= m || y >= n)return 0;
        if(obstacleGrid[x][y] == 1)return 0;
        if(mem[x][y]!=0)return mem[x][y];
        if(x == m-1 && y == n-1)return 1;
        
        mem[x][y] = findAllPath(x+1, y, m, n, mem, obstacleGrid) + findAllPath(x, y+1, m, n, mem, obstacleGrid);
        return mem[x][y];
    
    }
}
