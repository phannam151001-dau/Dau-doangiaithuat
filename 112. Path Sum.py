class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # Nếu là leaf node
        if not root.left and not root.right:
            return root.val == targetSum

        tong_con_lai = targetSum - root.val

        return (
            self.hasPathSum(root.left, tong_con_lai)
            or
            self.hasPathSum(root.right, tong_con_lai)
        )