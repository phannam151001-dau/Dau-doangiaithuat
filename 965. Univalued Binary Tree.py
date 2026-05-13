class Solution:
    def isUnivalTree(self, root):
        gia_tri_goc = root.val

        def duyet(node):
            if not node:
                return True

            if node.val != gia_tri_goc:
                return False

            return duyet(node.left) and duyet(node.right)

        return duyet(root)