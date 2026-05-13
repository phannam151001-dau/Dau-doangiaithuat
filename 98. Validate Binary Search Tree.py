class Solution:
    def isValidBST(self, root):

        def kiem_tra(node, nho_nhat, lon_nhat):
            if not node:
                return True

            if not (nho_nhat < node.val < lon_nhat):
                return False

            return (
                kiem_tra(node.left, nho_nhat, node.val)
                and
                kiem_tra(node.right, node.val, lon_nhat)
            )

        return kiem_tra(root, float("-inf"), float("inf"))