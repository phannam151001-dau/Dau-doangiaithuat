class Solution:
    def preorderTraversal(self, root):
        ket_qua = []

        def duyet(node):
            if not node:
                return

            ket_qua.append(node.val)
            duyet(node.left)
            duyet(node.right)

        duyet(root)

        return ket_qua