class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for n in nums:
            if abs(n) < abs(closest) or (abs(n) == abs(closest) and n > closest):
                closest = n
        return closest
        