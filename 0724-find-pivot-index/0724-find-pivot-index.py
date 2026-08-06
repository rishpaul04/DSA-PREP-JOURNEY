class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        right=0
        n=len(nums)
        s=sum(nums)
        if s-nums[0]==0:
            return 0
        for i in range(1,n):
            left+=nums[i-1]
            right=s-nums[i]-left
            if left==right:
                return i
        return -1
        