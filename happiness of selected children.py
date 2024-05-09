class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)  # Sort in descending order
        ans=0
        i = 0
        while k:
            ans += max(happiness[i] - i,0)
            i += 1
            k -= 1
        
        return ans
        
