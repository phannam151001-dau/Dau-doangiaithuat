class Solution:
    def buildTree(self, preorder, inorder):
        vi_tri = {}

        # Lưu vị trí của từng số trong inorder
        for i in range(len(inorder)):
            vi_tri[inorder[i]] = i

        self.chi_so = 0

        def tao_cay(trai, phai):
            if trai > phai:
                return None

            # Lấy root từ preorder
            gia_tri_root = preorder[self.chi_so]
            self.chi_so += 1

            node = TreeNode(gia_tri_root)

            # Tìm vị trí root trong inorder
            vi_tri_root = vi_tri[gia_tri_root]

            # Tạo cây trái và phải
            node.left = tao_cay(trai, vi_tri_root - 1)
            node.right = tao_cay(vi_tri_root + 1, phai)

            return node

        return tao_cay(0, len(inorder) - 1)