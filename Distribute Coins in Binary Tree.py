class Solution:
    def distributeCoinsUtil(self, root, ans):
        if not root:
            return 0
        
        l = self.distributeCoinsUtil(root.left, ans)
        r = self.distributeCoinsUtil(root.right, ans)
        
        ans[0] += abs(l) + abs(r)
        
        return root.val + l + r - 1

    def distributeCoins(self, root):
        ans = [0]
        self.distributeCoinsUtil(root, ans)
        return ans[0]
