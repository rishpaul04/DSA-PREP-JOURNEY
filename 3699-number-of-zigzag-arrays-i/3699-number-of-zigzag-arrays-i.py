class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        # Base cases for n = 1 (even though constraints state n >= 3)
        # up[j] means ending at value j with an increasing step
        # down[j] means ending at value j with a decreasing step
        up = [0] * m
        down = [0] * m
        
        # For the second element (i = 1), we look at transition from element 0
        # If element 1 is j, it is an up step if element 0 was < j (j choices)
        # It is a down step if element 0 was > j (m - 1 - j choices)
        for j in range(m):
            up[j] = j
            down[j] = m - 1 - j
            
        # Process from element 2 to n-1
        for i in range(2, n):
            next_up = [0] * m
            next_down = [0] * m
            
            # Compute prefix sums of down to optimize next_up
            # next_up[j] = sum(down[0...j-1])
            curr_sum = 0
            for j in range(m):
                next_up[j] = curr_sum % MOD
                curr_sum += down[j]
                
            # Compute suffix sums of up to optimize next_down
            # next_down[j] = sum(up[j+1...m-1])
            curr_sum = 0
            for j in range(m - 1, -1, -1):
                next_down[j] = curr_sum % MOD
                curr_sum += up[j]
                
            up = next_up
            down = next_down
            
        # The total number of arrays is the sum of all up and down states at index n-1
        return (sum(up) + sum(down)) % MOD
