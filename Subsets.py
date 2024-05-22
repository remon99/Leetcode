class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def dfs(i, temp):
            if i == len(nums):
                return l.append(temp)
                
            dfs(i + 1, temp + [nums[i]])
          
            dfs(i + 1, temp)
        
        dfs(0, [])
        return l
