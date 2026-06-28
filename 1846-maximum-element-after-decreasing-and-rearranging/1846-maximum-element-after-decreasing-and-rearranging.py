class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Step 1: Sort the array to allow for a greedy approach
        arr.sort()
        
        # Step 2: The first element must always be 1
        arr[0] = 1
        
        # Step 3: Enforce that adjacent elements differ by at most 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
                
        # Step 4: The last element will hold the maximum possible value
        return arr[-1]
