class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ans=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            if grid[i][0]==0:
                grid[i] = [1 if cell == 0 else 0 for cell in grid[i]]
            binary_string = ''.join(map(str, grid[i]))
            ans += int(binary_string, 2)
            
        
         
        for i in range(n):
            cnt=0
            for j in range(m):
                if grid[j][i]==1:
                    cnt+=1
            if cnt<=m//2:
                ans-=2**(n-1-i)*cnt
                ans+=2**(n-1-i)*(m-cnt)
            cnt=0
        return ans

            
