import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
            
        freq = [0] * 26
        odd_char = ""
        
        # Step 2: Extract the half-frequencies and identify the middle character if the string is odd
        for i in range(26):
            if counts[i] % 2 != 0:
                odd_char = chr(ord('a') + i)
            freq[i] = counts[i] // 2
            
        sz = len(s) // 2
        
        # Step 3: Helper function to compute the number of unique permutations
        # We cap the result at 10^6 + 1 to prevent huge integer computations, 
        # since max possible k is 10^6.
        def count_perms(freq_array, current_sz):
            ans = 1
            for f in freq_array:
                if f > 0:
                    ans *= math.comb(current_sz, f)
                    if ans > 1000000:
                        return 1000001
                    current_sz -= f
            return ans

        # Step 4: Check if k exceeds the total possible unique palindromes
        total_perms = count_perms(freq, sz)
        if k > total_perms:
            return ""
            
        left = []
        
        # Step 5: Greedily build the left half of the palindrome
        for _ in range(sz):
            for c in range(26):
                if freq[c] > 0:
                    # Tentatively choose this character
                    freq[c] -= 1
                    
                    # Calculate how many permutations can be formed with the remaining characters
                    cnt = count_perms(freq, sz - 1)
                    
                    if cnt >= k:
                        # If there are enough combinations to reach k, we lock in this character
                        left.append(chr(ord('a') + c))
                        sz -= 1
                        break
                    else:
                        # Otherwise, we subtract the combinations and backtrack to try the next character
                        k -= cnt
                        freq[c] += 1
                        
        # Step 6: Construct the final string by mirroring the left half
        left_str = "".join(left)
        return left_str + odd_char + left_str[::-1]