class Solution:
    def inorderTraversal(self, root):
        ket_qua = []

        def duyet(node):
            if not node:
                return

            duyet(node.left)
            ket_qua.append(node.val)
            duyet(node.right)

        duyet(root)

        return ket_qua