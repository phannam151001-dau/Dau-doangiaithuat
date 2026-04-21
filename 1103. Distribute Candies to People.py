class Solution(object):
    def distributeCandies(self, candies, num_people):
        res = [0] * num_people
        give = 1
        i = 0
        while candies > 0:
            res[i] += min(give, candies)
            candies -= give
            give += 1
            i = (i + 1) % num_people
        return res
        