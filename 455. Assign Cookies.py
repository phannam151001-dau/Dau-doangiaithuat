class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i = j = 0
        count = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1   # trẻ tiếp theo
            j += 1       # bánh tiếp theo
        return count