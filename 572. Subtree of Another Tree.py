class Solution:
    def isSubtree(self, root, subRoot):

        def giong_nhau(cay_1, cay_2):
            if not cay_1 and not cay_2:
                return True

            if not cay_1 or not cay_2:
                return False

            if cay_1.val != cay_2.val:
                return False

            return (
                giong_nhau(cay_1.left, cay_2.left)
                and
                giong_nhau(cay_1.right, cay_2.right)
            )

        if not root:
            return False

        if giong_nhau(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )