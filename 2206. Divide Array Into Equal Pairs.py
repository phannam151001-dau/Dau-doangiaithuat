class Solution(object):
    def divideArray(self, nums):
        count = Counter(nums)
        for v in count.values():
            if v % 2 != 0:
                return False
        return True
        