class Solution(object):
    def findTheDifference(self, s, t):
        cs = Counter(s)
        ct = Counter(t)
        for c in ct:
            if ct[c] > cs[c]:
                return c