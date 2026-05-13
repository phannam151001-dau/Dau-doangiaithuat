class Solution:
    def findTarget(self, root, k):
        da_gap = set()

        def duyet(node):
            if not node:
                return False

            if k - node.val in da_gap:
                return True

            da_gap.add(node.val)

            return duyet(node.left) or duyet(node.right)

        return duyet(root)