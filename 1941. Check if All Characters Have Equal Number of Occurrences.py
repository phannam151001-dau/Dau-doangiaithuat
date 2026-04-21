class Solution(object):
    def areOccurrencesEqual(self, s):
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        return len(set(count.values())) == 1
