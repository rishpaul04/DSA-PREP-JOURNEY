class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1
        for i in range(0,m):
            for j in range(0,n):
                if(obstacleGrid[i][j]==1):
                    dp[i][j]=0
                else:
                    if i>0:
                        dp[i][j]=dp[i-1][j]
                    if j>0:
                        dp[i][j]+=dp[i][j-1]
        return dp[m-1][n-1]