class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        left = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            # While the current window contains all three characters,
            # shrink it from the left to find the smallest valid window ending at 'right'
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                count[s[left]] -= 1
                left += 1
            
            # All substrings starting from index 0 up to left-1 and ending at right are valid
            res += left
            
        return res