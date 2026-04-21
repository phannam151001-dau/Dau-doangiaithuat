class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
        target = set(range(1, n + 1))
        for i in range(n):
            # kiểm tra hàng i
            if set(matrix[i]) != target:
                return False
            # kiểm tra cột i
            col = set(matrix[j][i] for j in range(n))
            if col != target:
                return False
        return True
        