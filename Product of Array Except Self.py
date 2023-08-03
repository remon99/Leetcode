class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]  
        mul = 1

        for i in range(len(nums) - 1):
            mul *= nums[i]
            res.append(mul)

        mul = 1
        
        for i in range(len(nums) - 2, -1, -1):
            mul *= nums[i + 1]
            res[i] *= mul

        return res