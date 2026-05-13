class Solution:
    def deleteDuplicates(self, head):
        hien_tai = head

        while hien_tai and hien_tai.next:
            if hien_tai.val == hien_tai.next.val:
                hien_tai.next = hien_tai.next.next
            else:
                hien_tai = hien_tai.next

        return head