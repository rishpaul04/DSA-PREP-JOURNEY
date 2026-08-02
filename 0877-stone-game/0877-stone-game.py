class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # Create an N x N DP table initialized to 0
        dp = [[0] * n for _ in range(n)]
        
        # Base case: When there is only 1 pile, the current player takes it
        for i in range(n):
            dp[i][i] = piles[i]
            
        # Iterate over different sub-problem lengths (from 2 to n)
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # The current player maximizes their score difference
                take_first = piles[i] - dp[i + 1][j]
                take_last = piles[j] - dp[i][j - 1]
                
                dp[i][j] = max(take_first, take_last)
                
        # If the score difference is greater than 0, Alice wins
        return dp[0][n - 1] > 0