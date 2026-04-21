class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        total = 0
        for i in range(len(cost)):
            if i % 3 != 2:   # viên thứ 3 (rẻ nhất trong nhóm) được miễn
                total += cost[i]
        return total
        