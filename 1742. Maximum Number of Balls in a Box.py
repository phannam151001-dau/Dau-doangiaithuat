class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        boxes = {}
        for i in range(lowLimit, highLimit + 1):
            box = sum(int(d) for d in str(i))
            boxes[box] = boxes.get(box, 0) + 1
        return max(boxes.values())
        