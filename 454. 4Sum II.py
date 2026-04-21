class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        ab_sum = Counter()
        # Tổng của nums1 và nums2
        for a in nums1:
            for b in nums2:
                ab_sum[a + b] += 1
        count = 0
        # Tổng của nums3 và nums4
        for c in nums3:
            for d in nums4:
                count += ab_sum[-(c + d)]
        return count