class Solution:
    def hasCycle(self, head):
        cham = head
        nhanh = head

        while nhanh and nhanh.next:
            cham = cham.next
            nhanh = nhanh.next.next

            if cham == nhanh:
                return True

        return False