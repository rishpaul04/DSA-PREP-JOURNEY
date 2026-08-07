class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Map to store prefix_sum -> first seen index
        seen = {0: -1}
        
        max_len = 0
        running_sum = 0
        
        for i, num in enumerate(nums):
            # Treat 1 as +1 and 0 as -1
            running_sum += 1 if num == 1 else -1
            
            if running_sum in seen:
                # Calculate subarray length
                max_len = max(max_len, i - seen[running_sum])
            else:
                # Store the first occurrence of this running sum
                seen[running_sum] = i
                
        return max_len