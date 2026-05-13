class Solution:
    def mergeTwoLists(self, list1, list2):
        node_gia = ListNode(0)
        hien_tai = node_gia

        while list1 and list2:
            if list1.val < list2.val:
                hien_tai.next = list1
                list1 = list1.next
            else:
                hien_tai.next = list2
                list2 = list2.next

            hien_tai = hien_tai.next

        if list1:
            hien_tai.next = list1
        else:
            hien_tai.next = list2

        return node_gia.next