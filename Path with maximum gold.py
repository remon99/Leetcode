class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def checkbound(i, j):
            return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])

        def getamount(i, j, sum=0):
            if checkbound(i, j) or (i, j) in s or grid[i][j] == 0:
                return sum
            s.add((i, j))
            sum += grid[i][j]
            max_gold = 0
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                max_gold = max(max_gold, getamount(i + di, j + dj, sum))
            s.remove((i, j))
            return max_gold

        max_gold = 0
        s = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, getamount(i, j))
        return max_gold
