class Solution(object):
    def countWords(self, words1, words2):
        c1 = Counter(words1)
        c2 = Counter(words2)
        count = 0
        for w in c1:
            if c1[w] == 1 and c2[w] == 1:
                count += 1
        return count
        