class Solution(object):
    def lengthOfLastWord(self, s):
        c=s.split()
        return len(c[-1])
        