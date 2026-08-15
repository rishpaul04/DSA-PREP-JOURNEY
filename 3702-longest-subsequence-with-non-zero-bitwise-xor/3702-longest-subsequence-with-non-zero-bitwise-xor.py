class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_sum = 0
        all_zeros = True
        
        for num in nums:
            xor_sum ^= num
            if num != 0:
                all_zeros = False
                
        if xor_sum != 0:
            return len(nums)
        
        if all_zeros:
            return 0
            
        return len(nums) - 1