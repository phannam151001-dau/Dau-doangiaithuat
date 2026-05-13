class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # Không có con trái
        if not root.left:
            return self.minDepth(root.right) + 1

        # Không có con phải
        if not root.right:
            return self.minDepth(root.left) + 1

        do_sau_trai = self.minDepth(root.left)
        do_sau_phai = self.minDepth(root.right)

        return min(do_sau_trai, do_sau_phai) + 1