class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s_rev = s[::-1]
        
        # dp array to store the LCS lengths of the current row
        # Space optimized from O(N^2) to O(N)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prev = 0  # Represents dp[i-1][j-1]
            for j in range(1, n + 1):
                temp = dp[j]  # Save current value before updating
                if s[i - 1] == s_rev[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp
                
        # The length of the Longest Palindromic Subsequence is dp[n]
        return n - dp[n]
