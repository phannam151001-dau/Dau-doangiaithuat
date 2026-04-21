class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        res = []
        for i in range(0, len(nums), 2):
            res.append(nums[i + 1])  # Bob
            res.append(nums[i])      # Alice
        return res
        