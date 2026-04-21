class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned = set(banned)
        word = ""
        count = {}
        for ch in paragraph.lower():
            if ch.isalpha():
                word += ch
            else:
                if word and word not in banned:
                    count[word] = count.get(word, 0) + 1
                word = ""
        # xử lý từ cuối cùng (nếu có)
        if word and word not in banned:
            count[word] = count.get(word, 0) + 1
        return max(count, key=count.get)