class Solution:
    def removeElements(self, head, val):
        node_gia = ListNode(0)
        node_gia.next = head

        hien_tai = node_gia

        while hien_tai and hien_tai.next:
            if hien_tai.next.val == val:
                hien_tai.next = hien_tai.next.next
            else:
                hien_tai = hien_tai.next

        return node_gia.next