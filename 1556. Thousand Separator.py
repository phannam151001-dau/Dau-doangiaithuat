class Solution(object):
    def thousandSeparator(self, n):
        s = str(n)
        res = []
        count = 0
        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
            count += 1
            if count == 3 and i != 0:
                res.append('.')
                count = 0
        return ''.join(res[::-1])
        