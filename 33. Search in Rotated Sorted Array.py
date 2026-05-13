class Solution:
    def search(self, nums, target):
        trai = 0
        phai = len(nums) - 1

        while trai <= phai:
            giua = (trai + phai) // 2

            if nums[giua] == target:
                return giua

            # Nửa trái đã sort
            if nums[trai] <= nums[giua]:
                if nums[trai] <= target < nums[giua]:
                    phai = giua - 1
                else:
                    trai = giua + 1

            # Nửa phải đã sort
            else:
                if nums[giua] < target <= nums[phai]:
                    trai = giua + 1
                else:
                    phai = giua - 1

        return -1