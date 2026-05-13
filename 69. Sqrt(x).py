class Solution:
    def mySqrt(self, x):
        trai = 0
        phai = x
        dap_an = 0

        while trai <= phai:
            giua = (trai + phai) // 2

            if giua * giua <= x:
                dap_an = giua
                trai = giua + 1
            else:
                phai = giua - 1

        return dap_an