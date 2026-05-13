class Solution:
    def postorderTraversal(self, root):
        ket_qua = []

        def duyet(node):
            if not node:
                return

            duyet(node.left)
            duyet(node.right)
            ket_qua.append(node.val)

        duyet(root)

        return ket_qua