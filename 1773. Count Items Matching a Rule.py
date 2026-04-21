class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):

        idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
        count = 0
        for item in items:
            if item[idx] == ruleValue:
                count += 1
        return count