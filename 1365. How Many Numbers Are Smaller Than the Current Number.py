class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        smaller = {}
        for i, num in enumerate(sorted_nums):
            if num not in smaller:
                smaller[num] = i   # số phần tử nhỏ hơn num
        return [smaller[num] for num in nums]