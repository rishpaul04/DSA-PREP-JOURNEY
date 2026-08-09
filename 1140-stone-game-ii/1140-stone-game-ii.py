from typing import List
from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums to quickly get the sum of remaining piles
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        @cache
        def dfs(i, m):
            # Base case: If we can take all remaining piles, take them all
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            res = 0
            # Try all possible moves for the current player (1 to 2m)
            for x in range(1, 2 * m + 1):
                # We want to maximize our stones, which is equivalent to 
                # minimizing the opponent's stones from the remaining piles.
                res = max(res, suffix_sum[i] - dfs(i + x, max(m, x)))
                
            return res
        
        # Alice starts at index 0 with M = 1
        return dfs(0, 1)