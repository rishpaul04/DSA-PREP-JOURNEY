class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Record the last occurrence of each character
        last_occ = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        # Step 2: Iterate through the string
        for i, char in enumerate(s):
            # If we've already included this character in our current path, skip it
            if char in seen:
                continue
                
            # Pop characters from the stack if they are larger than the current character
            # AND they appear again later in the string
            while stack and stack[-1] > char and last_occ[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add the current character to both our stack and tracking set
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)