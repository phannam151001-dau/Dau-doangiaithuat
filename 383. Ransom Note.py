class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = Counter(magazine)
        for c in ransomNote:
            if count[c] == 0:
                return False
            count[c] -= 1
        return True
        