class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta=[(n^k)-n for n in nums]
        res=sum(nums)

        delta.sort(reverse=True)
        for i in range(0,len(delta),2):
            if(i==len(delta)-1):
                break
            temp=delta[i]+delta[i+1]+res
            if(temp<res):
                break
            else:
                res=temp
        return res
