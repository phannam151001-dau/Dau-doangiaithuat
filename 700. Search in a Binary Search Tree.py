class Solution:
    def searchBST(self, root, val):
        hien_tai = root

        while hien_tai:
            if hien_tai.val == val:
                return hien_tai

            elif val < hien_tai.val:
                hien_tai = hien_tai.left

            else:
                hien_tai = hien_tai.right

        return None