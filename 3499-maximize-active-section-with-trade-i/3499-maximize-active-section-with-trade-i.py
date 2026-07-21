class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        
        # Augment the string as specified
        t = '1' + s + '1'
        
        # Group contiguous identical characters into (char, length) pairs
        blocks = []
        i = 0
        n = len(t)
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j
            
        max_delta = 0
        
        # Find every 1-block that is surrounded by 0-blocks on both sides
        for k in range(1, len(blocks) - 1):
            char, length = blocks[k]
            if char == '1' and blocks[k - 1][0] == '0' and blocks[k + 1][0] == '0':
                delta = blocks[k - 1][1] + blocks[k + 1][1]
                max_delta = max(max_delta, delta)
                
        return initial_ones + max_delta