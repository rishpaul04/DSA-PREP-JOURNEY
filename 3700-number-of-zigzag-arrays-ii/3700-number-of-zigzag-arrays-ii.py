class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        # Base case: if n = 1, any single element in [l, r] is valid
        if n == 1:
            return k
            
        # Base case: if n = 2, any pair of distinct elements is valid
        if n == 2:
            return (k * (k - 1)) % MOD
            
        # Size of the transition matrix
        m = 2 * k
        
        # Initialize the initial state vector V_2 for n = 2
        # V_2 contains [DP_up[0...k-1], DP_down[0...k-1]]
        V = [0] * m
        for u in range(k):
            V[u] = u               # Total elements smaller than u
            V[u + k] = k - 1 - u   # Total elements greater than u
            
        # Construct the transition matrix T
        T = [[0] * m for _ in range(m)]
        for u in range(k):
            # To get to DP_up[u], we sum DP_down[v] for all v < u
            for v in range(u):
                T[v + k][u] = 1
            # To get to DP_down[u], we sum DP_up[v] for all v > u
            for v in range(u + 1, k):
                T[v][u + k] = 1

        # Helper function to multiply two matrices under modulo
        def matrix_multiply(A, B):
            size = len(A)
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k_idx in range(size):
                    if A[i][k_idx] == 0:
                        continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k_idx] * B[k_idx][j]) % MOD
            return C

        # Helper function for modular matrix exponentiation
        def matrix_power(mat, power):
            size = len(mat)
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                result[i][i] = 1  # Identity matrix
                
            base = mat
            while power > 0:
                if power % 2 == 1:
                    result = matrix_multiply(result, base)
                base = matrix_multiply(base, base)
                power //= 2
            return result

        # Compute T^(n - 2)
        T_pow = matrix_power(T, n - 2)
        
        # Multiply V_2 * T^(n - 2) to get the final vector
        ans = 0
        for j in range(m):
            total_transitions = 0
            for i in range(m):
                total_transitions = (total_transitions + V[i] * T_pow[i][j]) % MOD
            ans = (ans + total_transitions) % MOD
            
        return ans
