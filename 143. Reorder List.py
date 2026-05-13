class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Tìm giữa
        cham = head
        nhanh = head

        while nhanh and nhanh.next:
            cham = cham.next
            nhanh = nhanh.next.next

        # Đảo ngược nửa sau
        truoc = None
        hien_tai = cham

        while hien_tai:
            ke_tiep = hien_tai.next
            hien_tai.next = truoc
            truoc = hien_tai
            hien_tai = ke_tiep

        # Trộn 2 nửa
        nua_dau = head
        nua_sau = truoc

        while nua_sau.next:
            tam_1 = nua_dau.next
            tam_2 = nua_sau.next

            nua_dau.next = nua_sau
            nua_sau.next = tam_1

            nua_dau = tam_1
            nua_sau = tam_2