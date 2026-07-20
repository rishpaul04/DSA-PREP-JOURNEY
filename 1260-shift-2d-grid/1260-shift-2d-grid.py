class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        total_elements=m*n
        k=k%total_elements
        result=[[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                new_flat_indx=(r*n+c+k)%total_elements
                new_r=new_flat_indx//n
                new_c=new_flat_indx%n
                result[new_r][new_c]=grid[r][c]
        return result
        