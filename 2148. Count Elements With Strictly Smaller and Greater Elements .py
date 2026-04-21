class Solution(object):
    def countElements(self, nums):
        mn = min(nums)
        mx = max(nums)
        count = 0
        for n in nums:
            if mn < n < mx:
                count += 1
        return count
        