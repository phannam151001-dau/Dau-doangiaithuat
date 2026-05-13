class Solution:
    def arrangeCoins(self, n):
        trai = 0
        phai = n
        dap_an = 0

        while trai <= phai:
            giua = (trai + phai) // 2
            so_dong_xu = giua * (giua + 1) // 2

            if so_dong_xu <= n:
                dap_an = giua
                trai = giua + 1
            else:
                phai = giua - 1

        return dap_an