class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # 1. Get unique elements and sort them
        unique_sorted = sorted(set(arr))
        
        # 2. Put them in a dictionary with their rank (1-indexed)
        ranks = {}
        for index, num in enumerate(unique_sorted):
            ranks[num] = index + 1
            
        # 3. Replace each number in the original array with its rank
        return [ranks[num] for num in arr]
