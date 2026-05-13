class Solution:
    def invertTree(self, root):
        if not root:
            return None

        # Đổi trái và phải
        root.left, root.right = root.right, root.left

        # Đảo tiếp cây con
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root