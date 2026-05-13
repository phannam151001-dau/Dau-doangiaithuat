class Solution:
    def findClosestElements(self, arr, k, x):
        trai = 0
        phai = len(arr) - k

        while trai < phai:
            giua = (trai + phai) // 2

            if x - arr[giua] > arr[giua + k] - x:
                trai = giua + 1
            else:
                phai = giua

        return arr[trai:trai + k]