class Solution:
    def firstBadVersion(self, n):
        trai = 1
        phai = n

        while trai < phai:
            giua = (trai + phai) // 2

            if isBadVersion(giua):
                phai = giua
            else:
                trai = giua + 1

        return trai