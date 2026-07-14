from math import gcd
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)
        
        @lru_cache(None)
        def dp(i, g1, g2):
            # Base case: if we've processed all elements
            if i == n:
                # Both subsequences must be non-empty (gcd > 0) and have equal gcd
                return 1 if g1 == g2 and g1 > 0 else 0
            
            # Choice 1: Skip the current element
            res = dp(i + 1, g1, g2)
            
            # Choice 2: Add the element to the first subsequence
            new_g1 = nums[i] if g1 == 0 else gcd(g1, nums[i])
            res = (res + dp(i + 1, new_g1, g2)) % MOD
            
            # Choice 3: Add the element to the second subsequence
            new_g2 = nums[i] if g2 == 0 else gcd(g2, nums[i])
            res = (res + dp(i + 1, g1, new_g2)) % MOD
            
            return res
        
        # Start from index 0, with both subsequences initially empty (gcd = 0)
        return dp(0, 0, 0)