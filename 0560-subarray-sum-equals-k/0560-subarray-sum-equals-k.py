class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        current_sum=0
        prefix_sum={0:1}
        for num in nums:
            current_sum+=num
            if current_sum-k in prefix_sum:
                count+=prefix_sum[current_sum-k]
            if current_sum in prefix_sum:
                prefix_sum[current_sum]+=1
            else:
                prefix_sum[current_sum]=1
        return count





        