class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        memo = {}
        
        def fun(i: int, can_rob: int) -> int:
            # Base case: reached the end of the street
            if i >= n:
                return 0
                
            # Check if we have already calculated this exact scenario
            if (i, can_rob) in memo:
                return memo[(i, can_rob)]
                
            # 1. If we robbed the previous house (can_rob == 0), we MUST skip this one.
            if can_rob == 0:
                memo[(i, can_rob)] = fun(i + 1, 1)
                return memo[(i, can_rob)]  # CRITICAL FIX: You must return here!
                
            # 2. We are allowed to rob this house (can_rob == 1). We have two choices.
            
            # Choice 1 (c1): Rob current house, move to i+1 with flag 0 (cannot rob next)
            c1 = nums[i] + fun(i + 1, 0)
            
            # Choice 2 (c2): Skip current house, move to i+1 with flag 1 (safe to rob next)
            c2 = fun(i + 1, 1)
            
            # Return the maximum of both choices
            memo[(i, can_rob)] = max(c1, c2)
            return memo[(i, can_rob)]
            
        # Start at index 0, with full permission to rob (flag = 1)
        return fun(0, 1)