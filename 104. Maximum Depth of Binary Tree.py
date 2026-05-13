class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        do_sau_trai = self.maxDepth(root.left)
        do_sau_phai = self.maxDepth(root.right)

        return max(do_sau_trai, do_sau_phai) + 1