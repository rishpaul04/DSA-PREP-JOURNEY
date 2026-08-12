class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Add the current element to the window's frequency map
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # If the frequency exceeds k, shrink the window from the left
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
                
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length