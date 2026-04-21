class Solution(object):
    def sumOfUnique(self, nums):
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        total = 0
        for k in count:
            if count[k] == 1:
                total += k
        return total
        