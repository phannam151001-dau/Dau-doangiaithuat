class Solution:
    def findMin(self, nums):
        ben_trai = 0
        ben_phai = len(nums) - 1

        while ben_trai < ben_phai:
            o_giua = (ben_trai + ben_phai) // 2

            if nums[o_giua] > nums[ben_phai]:
                ben_trai = o_giua + 1
            else:
                ben_phai = o_giua

        return nums[ben_trai]