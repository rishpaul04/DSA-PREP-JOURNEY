class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        frequency={}
        for char in text:
            frequency[char]=frequency.get(char,0)+1
#         The word "balloon" requires the following character counts:

# b → 1
# a → 1
# l → 2
# o → 2
# n → 1
        return min(
            frequency.get('b', 0),
            frequency.get('a', 0),
            frequency.get('l', 0) // 2,  # Requires 2, so integer divide by 2
            frequency.get('o', 0) // 2,  # Requires 2, so integer divide by 2
            frequency.get('n', 0)
        )
        