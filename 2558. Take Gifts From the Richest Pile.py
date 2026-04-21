class Solution(object):
    def pickGifts(self, gifts, k):
        # tạo max heap bằng cách đổi dấu
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            largest = -heapq.heappop(heap)
            new_val = int(math.sqrt(largest))
            heapq.heappush(heap, -new_val)
        return -sum(heap)
        