class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Step 1: Generate prefix sums of transformed +1/-1 values
        prefix_sum = 0
        
        # Since prefix sums can be negative, we use a coordinate shift or a hash map/frequency array.
        # Max possible range of prefix sum with N <= 1000 is [-1000, 1000].
        # We use an offset of 1001 to keep indices positive.
        OFFSET = 1005
        
        # Fenwick Tree (Binary Indexed Tree) to count elements less than current prefix_sum
        bit = [0] * (2 * OFFSET + 2)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
        
        # Initialize with P[0] = 0
        update(0 + OFFSET, 1)
        
        ans = 0
        for num in nums:
            # Step 2: Update current prefix sum
            prefix_sum += 1 if num == target else -1
            
            # Step 3: Count all previous prefix sums strictly less than the current one
            # P[L] < P[R+1] -> query up to (prefix_sum + OFFSET - 1)
            ans += query(prefix_sum + OFFSET - 1)
            
            # Insert the current prefix sum into the BIT
            update(prefix_sum + OFFSET, 1)
            
        return ans
