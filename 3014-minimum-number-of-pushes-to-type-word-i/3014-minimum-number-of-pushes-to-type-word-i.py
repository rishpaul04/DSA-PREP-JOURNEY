class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        
        # We can map up to 8 letters at each push cost level (1 push, 2 pushes, etc.)
        for i in range(n):
            # i // 8 determines the "layer" of the key. 
            # Layer 0 costs 1 push, layer 1 costs 2 pushes, etc.
            total_pushes += (i // 8) + 1
            
        return total_pushes