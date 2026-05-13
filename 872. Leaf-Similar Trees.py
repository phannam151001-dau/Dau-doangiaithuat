class Solution:
    def leafSimilar(self, root1, root2):

        def lay_la(node, danh_sach_la):
            if not node:
                return

            # Nếu là leaf node
            if not node.left and not node.right:
                danh_sach_la.append(node.val)
                return

            lay_la(node.left, danh_sach_la)
            lay_la(node.right, danh_sach_la)

        la_cay_1 = []
        la_cay_2 = []

        lay_la(root1, la_cay_1)
        lay_la(root2, la_cay_2)

        return la_cay_1 == la_cay_2