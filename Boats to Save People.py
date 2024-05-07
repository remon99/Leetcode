class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        sum=0
        left,right=0,len(people)-1
        res=0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # Move the left pointer if both people can fit in the boat
            right -= 1  # Always move the right pointer

            res += 1  # Increment the count of boats

        return res
