class Solution:
    def removeNthFromEnd(self, head, n):
        node_gia = ListNode(0)
        node_gia.next = head

        cham = node_gia
        nhanh = node_gia

        # nhanh đi trước n + 1 bước
        for i in range(n + 1):
            nhanh = nhanh.next

        # cùng đi
        while nhanh:
            cham = cham.next
            nhanh = nhanh.next

        # xóa node
        cham.next = cham.next.next

        return node_gia.next