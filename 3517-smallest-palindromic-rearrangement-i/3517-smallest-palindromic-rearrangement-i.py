from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Count the frequency of each character
        counts = Counter(s)
        
        first_half = []
        mid_char = ""
        
        # Iterate through the alphabet to ensure lexicographically smallest order
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in counts:
                # If the frequency is odd, this character will be in the middle
                if counts[char] % 2 != 0:
                    mid_char = char
                
                # Append half of the occurrences to our first half
                first_half.append(char * (counts[char] // 2))
                
        # Join the list into a string
        first_half_str = "".join(first_half)
        
        # The result is the first half + middle character + reversed first half
        return first_half_str + mid_char + first_half_str[::-1]