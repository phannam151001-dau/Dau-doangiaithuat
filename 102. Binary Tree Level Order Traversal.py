from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        ket_qua = []
        hang_doi = deque([root])

        while hang_doi:
            so_node = len(hang_doi)
            tang_hien_tai = []

            for i in range(so_node):
                node = hang_doi.popleft()
                tang_hien_tai.append(node.val)

                if node.left:
                    hang_doi.append(node.left)

                if node.right:
                    hang_doi.append(node.right)

            ket_qua.append(tang_hien_tai)

        return ket_qua