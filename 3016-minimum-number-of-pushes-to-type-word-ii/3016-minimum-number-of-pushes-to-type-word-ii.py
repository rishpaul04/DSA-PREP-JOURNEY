from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count the frequency of each letter in the word
        counts = Counter(word)
        
        # Step 2: Sort the frequencies in descending order
        sorted_counts = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        
        # Step 3: Calculate the total pushes using a greedy approach
        for i, count in enumerate(sorted_counts):
            # The number of pushes needed is determined by the index
            # (i // 8) + 1 evaluates to:
            # 1 for i in 0-7, 2 for i in 8-15, 3 for i in 16-23, etc.
            pushes = (i // 8) + 1
            total_pushes += count * pushes
            
        return total_pushes