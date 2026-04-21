class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        for w in words:
            if w.startswith(pref):
                count += 1
        return count
        