class Solution:
    def findMode(self, root):
        dem = {}

        def duyet(node):
            if not node:
                return

            if node.val in dem:
                dem[node.val] += 1
            else:
                dem[node.val] = 1

            duyet(node.left)
            duyet(node.right)

        duyet(root)

        xuat_hien_nhieu_nhat = max(dem.values())
        ket_qua = []

        for so in dem:
            if dem[so] == xuat_hien_nhieu_nhat:
                ket_qua.append(so)

        return ket_qua