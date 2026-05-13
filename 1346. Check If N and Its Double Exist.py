class Solution:
    def checkIfExist(self, arr):
        da_thay = set()

        for so in arr:
            if so * 2 in da_thay:
                return True

            if so % 2 == 0 and so // 2 in da_thay:
                return True

            da_thay.add(so)

        return False