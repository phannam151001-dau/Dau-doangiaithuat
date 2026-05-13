class Solution:
    def maxProfit(self, prices):
        gia_thap_nhat = prices[0]
        loi_nhuan_max = 0

        for gia_hien_tai in prices:
            if gia_hien_tai < gia_thap_nhat:
                gia_thap_nhat = gia_hien_tai

            loi_nhuan = gia_hien_tai - gia_thap_nhat

            if loi_nhuan > loi_nhuan_max:
                loi_nhuan_max = loi_nhuan

        return loi_nhuan_max