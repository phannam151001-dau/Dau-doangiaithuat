class Solution:
    def pivotInteger(self, n):
        tong = n * (n + 1) // 2
        can_bac_hai = int(tong ** 0.5)

        if can_bac_hai * can_bac_hai == tong:
            return can_bac_hai

        return -1