class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left < right:
            if height[left]<height[right]:
                area=(right-left)* min(height[left],height[right])
                max_area=max(area,max_area)
                left+=1
            else:
                area=(right-left)* min(height[left],height[right])
                max_area=max(area,max_area)
                right-=1
        return max_area

        