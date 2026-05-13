class Solution:
    def checkTree(self, root):
        tong_con = root.left.val + root.right.val

        return root.val == tong_con