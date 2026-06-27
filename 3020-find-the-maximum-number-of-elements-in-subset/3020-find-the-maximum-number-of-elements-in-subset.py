from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 1
        
        # Case 1: Handle the number 1 separately
        if 1 in count:
            c = count[1]
            # Must be an odd number of elements
            max_len = max(max_len, c if c % 2 != 0 else c - 1)
        
        # Case 2: Handle numbers > 1
        for num in count:
            if num == 1:
                continue
                
            current_len = 0
            x = num
            
            # Keep climbing up the chain x -> x^2 -> x^4 as long as we have >= 2 elements
            while x in count and count[x] >= 2:
                current_len += 2
                x = x * x
                
            # If the final element exists at least once, it can be the peak
            if x in count:
                current_len += 1
            else:
                # If it doesn't exist, the previous element must become the peak 
                # (we take back 1 from the 2 we claimed for it)
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len