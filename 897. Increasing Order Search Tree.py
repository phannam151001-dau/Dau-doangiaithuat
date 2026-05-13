class Solution:
    def increasingBST(self, root):
        node_gia = TreeNode(0)
        self.hien_tai = node_gia

        def duyet(node):
            if not node:
                return

            duyet(node.left)

            node.left = None
            self.hien_tai.right = node
            self.hien_tai = node

            duyet(node.right)

        duyet(root)

        return node_gia.right