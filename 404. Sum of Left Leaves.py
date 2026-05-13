class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        tong = 0

        # Kiểm tra lá bên trái
        if root.left:
            if not root.left.left and not root.left.right:
                tong += root.left.val

        tong += self.sumOfLeftLeaves(root.left)
        tong += self.sumOfLeftLeaves(root.right)

        return tong