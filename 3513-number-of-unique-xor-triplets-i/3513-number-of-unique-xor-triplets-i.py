class Solution:

  def uniqueXorTriplets(self, nums: list[int]) -> int:
    n = len(nums)

    if n <= 2:
      return n

    # For n >= 3, the result is 2^(bit_length(n))
    return 1 << n.bit_length()