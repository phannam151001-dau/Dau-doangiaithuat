class Solution:
    def addTwoNumbers(self, l1, l2):
        node_gia = ListNode(0)
        hien_tai = node_gia
        so_nho = 0

        while l1 or l2 or so_nho:
            gia_tri_1 = 0
            gia_tri_2 = 0

            if l1:
                gia_tri_1 = l1.val
                l1 = l1.next

            if l2:
                gia_tri_2 = l2.val
                l2 = l2.next

            tong = gia_tri_1 + gia_tri_2 + so_nho
            so_nho = tong // 10

            hien_tai.next = ListNode(tong % 10)
            hien_tai = hien_tai.next

        return node_gia.next