class Solution(object):
    def sortEvenOdd(self, nums):
        even = sorted(nums[::2])          # index chẵn
        odd = sorted(nums[1::2], reverse=True)  # index lẻ
        res = []
        i = j = 0
        for idx in range(len(nums)):
            if idx % 2 == 0:
                res.append(even[i])
                i += 1
            else:
                res.append(odd[j])
                j += 1
        return res