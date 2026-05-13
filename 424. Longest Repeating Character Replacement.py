class Solution:
    def characterReplacement(self, s, k):
        dem_ky_tu = {}
        trai = 0
        xuat_hien_nhieu_nhat = 0
        do_dai_max = 0

        for phai in range(len(s)):
            ky_tu = s[phai]

            if ky_tu in dem_ky_tu:
                dem_ky_tu[ky_tu] += 1
            else:
                dem_ky_tu[ky_tu] = 1

            if dem_ky_tu[ky_tu] > xuat_hien_nhieu_nhat:
                xuat_hien_nhieu_nhat = dem_ky_tu[ky_tu]

            while (phai - trai + 1) - xuat_hien_nhieu_nhat > k:
                dem_ky_tu[s[trai]] -= 1
                trai += 1

            do_dai = phai - trai + 1

            if do_dai > do_dai_max:
                do_dai_max = do_dai

        return do_dai_max