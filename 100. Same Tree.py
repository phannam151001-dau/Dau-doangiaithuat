class Solution:
    def isSameTree(self, p, q):
        # Cả hai đều rỗng
        if not p and not q:
            return True

        # Một cây rỗng
        if not p or not q:
            return False

        # Giá trị khác nhau
        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )