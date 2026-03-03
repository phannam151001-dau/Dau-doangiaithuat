class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result