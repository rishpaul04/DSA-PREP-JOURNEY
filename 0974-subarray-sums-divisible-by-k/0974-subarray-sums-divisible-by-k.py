class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        remainder_counts={0:1}
        current_sum=0
        for num in nums:
            current_sum+=num
            remainder=current_sum%k
            if remainder in remainder_counts:
                count+=remainder_counts[remainder]
            if remainder in remainder_counts:
                remainder_counts[remainder]+=1
            else:
                remainder_counts[remainder]=1
        return count

