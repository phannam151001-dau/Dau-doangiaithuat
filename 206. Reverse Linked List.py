class Solution:
    def reverseList(self, head):
        truoc = None
        hien_tai = head

        while hien_tai:
            ke_tiep = hien_tai.next
            hien_tai.next = truoc
            truoc = hien_tai
            hien_tai = ke_tiep

        return truoc