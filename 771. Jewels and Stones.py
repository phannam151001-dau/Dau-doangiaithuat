class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        count = 0
        for c in stones:
            if c in jewel_set:
                count += 1
        return count
        