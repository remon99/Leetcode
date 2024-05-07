class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while nums[i]<0:
            if(abs(nums[i])) in nums:
                return abs(nums[i])
            if i==len(nums)-1:
                return -1
            i+=1

        return -1
